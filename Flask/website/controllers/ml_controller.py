import numpy as np
import cv2, pickle, pytesseract, base64


class Ocrcontroller:

    def detect_biggest_font(self, result_text_no_paragraph):

        #list of the rectangle values
        height_list = []
        divided_width = []

        top_high_val = []
        top_width_val = []

        #save text for brand
        text_for_brand = []

        for detection in result_text_no_paragraph: 

            top_left = tuple(detection[0][0])
            bottom_right = tuple(detection[0][2])
            bottom_left = tuple(detection[0][3])

            height_list.append(np.subtract(bottom_left[1],top_left[1]))

            width_sentence = np.subtract(bottom_right[0],bottom_left[0])

            len_sentence = len(detection[1])

            boldest_font = np.divide(len_sentence, width_sentence)

            divided_width.append(boldest_font)

            text_for_brand.append(detection[1])


        #one highest values
        highest_values = list(set(height_list))
        
        highest_values = sorted(highest_values, reverse=True)[:2]

        #one boldest font values
        widthest_values = list(set(divided_width))
        widthest_values = sorted(widthest_values, reverse=False)[:2]

        #find indexes of widthest three values in divided_width list

        for width in divided_width:
            if width in widthest_values:
                index_of_width = divided_width.index(width)
                top_width_val.append(result_text_no_paragraph[index_of_width][1])

        for height in highest_values:
            if height in highest_values:
                index_of_height = height_list.index(height)
                top_high_val.append(result_text_no_paragraph[index_of_height][1])

        #title_candidates = list(set(top_width_val).intersection(top_high_val))

        #calling the function to sort out the digits
        biggest_font = top_high_val

        return biggest_font


    #detect the text in image with paragraphs
    def image_text(self, result_text_in_image):

        text_paragraph = []

        for sentence in result_text_in_image:

            text_paragraph.append(sentence[1])

        return text_paragraph


    #on the webapplication there are drawn some rectangles into the picutre
    def draw_rectangle(self, result_text_in_image, image_path):

      img = cv2.imread(image_path)

      for detection in result_text_in_image: 

        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        img = cv2.rectangle(img, top_left, bottom_right,(0,255,0),3)

        def ndarray_to_b64(ndarray):
   
          img = cv2.cvtColor(ndarray, cv2.COLOR_RGB2BGR)
          _, buffer = cv2.imencode('.png', img)
          return base64.b64encode(buffer).decode('utf-8')

        base64_image = ndarray_to_b64(img)

      return base64_image


    #this function removes single or pair words in the image text
    def remove_single_words(self, text_paragraph, title_length):

      no_lonely_words = []

      for word in text_paragraph:

        word_list = word.split()

        if len(word_list) > title_length:

          no_lonely_words.append(word_list)
      
      def join_list(no_lonely_words):

        result_list = []

        for word in no_lonely_words:

          word = ' '.join(word)
          word = word.lower()
          result_list.append(word)

        return result_list
      
      specified_word_list = join_list(no_lonely_words)
    
      return specified_word_list



#controlls methods for the title extraction
class TitleExtractionController:


    def load_title_model(self):
        #the model is loaded 
        filename_model = "C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/ml_models/title_classification/models/best_model.sav"
        loaded_title_model = pickle.load(open(filename_model, 'rb'))

        #the vectroizer which turns the words into vectors is loaded
        filename_vectorizer = "C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/ml_models/title_classification/vectorizers/best_vectorizer.sav"
        loaded_title_vectorizer = pickle.load(open(filename_vectorizer, 'rb'))

        return loaded_title_model, loaded_title_vectorizer


    def get_title_of_result(self, model_results):

        model_title_column = []

        for sentence in model_results:
          model_title_column.append(sentence[1])

        #the lists are turned into a numpay array
        model_title_column = np.array(model_title_column)

        #finds the biggest probability and its index
        idx_model = np.argpartition(model_title_column, -1)[-1:]
        end_result_title = idx_model[np.argsort((-model_title_column)[idx_model])]

        return end_result_title

    
    def get_description_of_result(self, model_results):

        #two lists where description and title candidates are saved
        model_description_column = []
    
        #the result of the model exists of two columns the first columns are the probabilities that the element is a title and
        #the second column is the probability that the element is a description

        for sentence in model_results:
          model_description_column.append(sentence[0])

        model_description_column = np.array(model_description_column)

        idx_model = np.argpartition(model_description_column, -1)[-1:]
        end_result_description = idx_model[np.argsort((-model_description_column)[idx_model])]

        return end_result_description


class PriceExtractionController:

    def load_ocr_model(self, filename):

        pytesseract.pytesseract.tesseract_cmd = r"C:/Users/mario.vonbassen/tesseract.exe"

        #TODO change to base64_image

        img = cv2.imread(f"C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/static/uploads/{filename}")
        

        custom_config = r'--oem 3 --psm 6'
        price_text = pytesseract.image_to_string(img, config=custom_config)

        price_text = price_text.split()

        price_text = list(set(price_text))

        return price_text


    #function to find frequent currencies in imagetext
    def frequent_currency(self, currency_list):

        if len(currency_list) != 0: 
          return max(set(currency_list), key = currency_list.count)
        else:
          return "no Price!"


    #!!!!!!!!!!!!!!!!!!!!!!!!!!
#TODO add more currencies
      #transform the currency symbol to ISO-Text for Schema.org
    def currency_symbol_to_text(self, most_frequent_currency):

        if most_frequent_currency == "£":
          currency_text = "GBP"

        elif most_frequent_currency == "$":
          currency_text = "USD"

        elif most_frequent_currency == "€":
          currency_text = "EUR"

        else:
          return most_frequent_currency

        return currency_text

