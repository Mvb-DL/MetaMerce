import spacy, easyocr, cv2, pickle, pycountry
import pandas as pd
from price_parser import Price
from .controllers.ml_controller import Ocrcontroller, TitleExtractionController, PriceExtractionController

OCR = Ocrcontroller()
TEC = TitleExtractionController()
PEC = PriceExtractionController()


#this function is to preprocess the uploaded image by the user
def preprocessing_image(image_path):

    image_gray = cv2.imread(image_path, 0)

    return image_gray


#deploy the ocr model to find the brand of the product
reader = easyocr.Reader(['en'], gpu=False)


#Deploy the OCR Model
def ocr_model(filename, title_length):
    
    #TODO
    image_path = f"C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/static/uploads/{filename}"

    #image_gray = preprocessing_image(image_path)

    #to get the biggest rectangle
    #result_text_no_paragraph = reader.readtext(image_gray, paragraph=False, height_ths=0.5, width_ths=1)

    #text in paragraphs in image
    result_text_in_image = reader.readtext(image_path, paragraph=True, slope_ths=0, ycenter_ths=0, height_ths=0, y_ths=0.5, x_ths=1, batch_size=32)

    #calls OCR Class with draw rectangle method
    base64_image = OCR.draw_rectangle(result_text_in_image, image_path)

    #title_candidates, text_non_paragraph = detect_title_candidates(result_title)
    text_paragraph = OCR.image_text(result_text_in_image)   
    
    #calls OCR Class with method
    specified_word_list = OCR.remove_single_words(text_paragraph, title_length)
    
    return text_paragraph, specified_word_list, base64_image


#this function extracts the title in the imagetext
def title_extraction(imagetext):
  
  title_model, title_vectorizer = TEC.load_title_model()

  predict_title = title_vectorizer.transform(imagetext)
  model_results = title_model.predict_proba(predict_title)

  end_result_title = TEC.get_title_of_result(model_results)
  end_result_description = TEC.get_description_of_result(model_results)

  #the imagetetxt ist turned into a list
  imagetext = list(imagetext)

  title = []
  description = []

  for i in end_result_title:
    title.append(imagetext[i])

  for i in end_result_description:
    description.append(imagetext[i])

  #the title and description are returned
  return title, description



#function to extract the category
def category_extraction(title_candidates):

  category_result = []

  #this are the following categories that exist for the application
  categories = ['all beauty', 'added_category', 'amazon home', 'apple',
       'appliances', 'arts', 'automotive', 'books', 'camera and photo',
       'cds and vinyl', 'cell phones accessories',
       'clothing, shoes and jewelry', 'digital music', 'electronics',
       'fashion', 'gift cards', 'grocery and gourmet food', 'kitchen',
       'industrial and scientific', 'kindle', 'luxury', 'magazines',
       'movies and tv', 'musical instruments', 'office products',
       'pantry', 'garden', 'pet supplies', 'software',
       'sports and outdoors', 'tools and home improvement',
       'toys and games', 'video games']

  def load_model():

    #category vectorizer
    filename_vectorizer = "C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/ml_models/category_classification/category_vectorizer.sav"
    category_vectorizer = pickle.load(open(filename_vectorizer, 'rb'))

    #category model
    category_model_filename = "C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/ml_models/category_classification/category_model.sav"
    category_model = pickle.load(open(category_model_filename, 'rb'))

    return category_model, category_vectorizer


  category_model, category_vectorizer = load_model()

  predict_title = category_vectorizer.transform(title_candidates)

  category_model_result = category_model.predict(predict_title)
 
  category_model_result  = categories[int(category_model_result[0])]
  
  #two categories are returned when both models predicts the same only one category is given back
  category_result.append(category_model_result )

  return list(category_result)




#function to extract the brand from title
def brand_extraction(title_candidates):

    #load the trained model
    brand_nlp = spacy.load("C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/ner_spacy/output/brand_model_best")

    brands_entities = []
    
    #sets the brand none that it gets only returned if it´s not none
    brand = None

    for title in title_candidates:

      #loads the spacy model and finds the title entity
      doc = brand_nlp(title)
      
      for ent in doc.ents:

          brands_entities.append((ent.label_, ent.text))
          df = pd.DataFrame(brands_entities, columns=('named entity', 'output'))
          BRAND_named_entity = df.loc[df['named entity'] == 'BRAND']["output"]
          brand = BRAND_named_entity

    if brand is not None:

      return list(brand)
    
    else:

      brands = "None"
      return brands


#function to extract the price from text
def price_extraction(filename):

      price_text = PEC.load_ocr_model(filename)

      #list for all existing prices
      price_list = []

      #list for all existing currencies
      currency_list = []

      #highest and lowest price in imagetext
      high_low_price = []

      for price in price_text:

        #calls the lib to extract prices from a string
        extracted_price = Price.fromstring(price)

        #filters found text. only if the price is not null or not zero it gots appended
        if extracted_price.amount_text and extracted_price.amount_text != "0" and extracted_price.currency is not None:

          if extracted_price.currency == "£" or extracted_price.currency == "$" or extracted_price.currency == "€":
          
            price = extracted_price.amount_text + extracted_price.currency

            high_low_price.append(extracted_price.amount_float)

            price_list.append(price)

            currency_list.append(extracted_price.currency)


      most_frequent_currency = PEC.frequent_currency(currency_list)

      currency = PEC.currency_symbol_to_text(most_frequent_currency)

      price_list = list(set(price_list))


      if len(high_low_price) > 0:

        lowPrice = str(min(high_low_price))
        highPrice = str(max(high_low_price))

        lowPrice = lowPrice + most_frequent_currency
        highPrice = highPrice + most_frequent_currency
      
      else:

        lowPrice = None
        highPrice = None

      return price_list, currency, price_text, lowPrice, highPrice



#function to extract countries from text
def country_extraction(imagetext, imagetext_two):

  product_countries = []

  imagetext = ' '.join(imagetext)
  imagetext_two = ' '.join(imagetext_two)

  for country in pycountry.countries:

      #find countryname in text
      if country.name in str(imagetext) or country.name in str(imagetext_two):
        product_countries.append(country.name)

  product_countries = list(set(product_countries))

  return product_countries