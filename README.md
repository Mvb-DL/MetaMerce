
Specification


Project Title	Automated content tagging, classification, and construction of a knowledge graph of the assortment in an e-commerce store based on ML
Responsible person	Mario von Bassen
Start	01.09.2022
Last Change	X
Status	In Progress


Change history

Nr.	Date	Version	Change	Type of change
1				
2				
3				
4				
5				

 
Content
1	Introduction Summary Use-Case	4
2	General	4
1.1	Project Scope	4
1.2	Background of the Project	4
1.3	Problem Definition	5
1.4	Solution Approaches	5
1.5	Interfaces and Frameworks	6
2	Concept	7
2.1	Goal of the Provider	7
2.2	Goal of the User	7
2.3	Stakeholders and Personas	7
2.4	Software and Hardware Requirements of the Users	7
3	Functional Requirements	8
4	Non-Functional Requirements	8
4.1	General Requirements	8
4.2	Legal Requirements	9
4.3	Technical Requirements	9
5	General Conditions	9
5.1	Timetable	9
5.2	Technical Requirements	9
5.3	Risk Analyses	10
5.3.1	Dependencies to other Frameworks, Packages…	10
5.4	Quality and Testing	10
6	Data situation	11
7	Definition of Done	11
8	Attachments	11
Functional Requirements of the Frontend	12
9	High-Fidelity Prototype Frontend	13
10	Use Case Diagram	15
The user can easily upload his product and the system identifies to product. After this it creates the meta tags and saves the output, sends it back to the user and building/showing the knowledge graph to the user.	15
11	Class Diagram	16
12	Sequence Diagrams	16
13	Activity Diagram	18
14	Database Schema	18
15	Question Catalog	19

 
1	Introduction Summary Use-Case

As a first step, the application should independently identify or classify products (possibly also reviews) of a webshop as products and differentiate them from other content elements with the help of an AI model. For this purpose, a web application is to be operated as an interface by the user in order to upload the content for evaluation. As a next step, the application should assign metatags to the identified products of the webshop and expand these products using meta descriptions that follow the schema.org standard. The individual content components are classified according to different types: e.g. Product, Offer and Review (https://schema.org/docs/schemas.html). These different types have clear and definable characteristics, which in turn have certain characteristic values. There are a large number of accessible datasets for the identification and classification of products or reviews. In addition, there are extensive data sets of already meta-described products according to the Schema.org standard. As a third step, an individual knowledge graph of the products of the webshop and a semantic webshop will be built by assigning metatags. The knowledge graph of the products can then also be used for analytical evaluation of the web shop operator. In addition, the search engine ranking of tagged websites increases and up-selling and cross-selling can be used in a more targeted manner. 

2	General

1.1	Project Scope

The goal is to develop an application which can be used by external users to upload products of their webshops within this application. It is the task of the system to filter this input, to extract the required data and, based on existing data using a trained machine learning model, to identify whether the input is a product, to determine the product category, the individual features and feature characteristics. Subsequently, it should be possible for the system to output the respective meta tags according to the Schema.org standard and, if necessary, to create a knowledge graph about the individual assortments.

1.2	Background of the Project

A common language between website and search engine already exists. 
The next step is to develop an application that makes as many web pages as possible understandable for the search engine. I should be easy and motivative to use the application to build up his own semantic website as website host.


1.3	Problem Definition

	The main problem is that the search engine does not understand what is on a web page.
	For better search results, the search engine must understand the semantics of the content on the Internet. 
	The insertion of structured data is difficult for many website hosts, because they often have no experience with code.
	Complicated links between entities are not apparent.
	Many e-commerce stores are so large that the operators lose track of which products they offer on their website.
	Often it is not noticed that many products do not fit into the rest of the assortment and to give recommendations for similar products.
	The truthfulness and completeness of individual entities cannot be verified so easily.

1.4	Solution Approaches

	Structured data such as Schema.org enables various ML algorithms to capture the semantics of content
	The system is intended to be very user-friendly and thus encourage users to upload the content of their website and mark it up with structured data.
	The automated creation of a Knowledge Graph allows to have a graphical overview of the existing products and connections between the products. 
	If necessary, it is possible to display products not only in tabular form but also graphically
	Recommender System and Anomaly Detection are largely based on existing structured data.
	Structured data plays an essential role for search engine ranking and rich snippets.
	By breaking down content to individual entities, facts can be quickly verified.

1.5	Interfaces and Frameworks

Interfaces
The application requires several interfaces. On the one hand from the frontend to the backend and the backend in turn to the AI model and so on as you can see in the list below.
•	Frontend to Backend
•	Backend to Database
•	Backend to Model
•	Model to Database

Frameworks
For the application several frameworks are used. The programming language is in Python and probably R for the Model. Below is shown a list of several frameworks which are used for building the application. For the frontend it is goal to use as less as possible and to reduce it on using HTML, CSS and JS. If necessary Bootstrap, jQuery or React.
•	Django or Flask
•	JQuery/React
•	NumPY
•	Pandas
•	Sci-Kit Learn
•	Tensorflow
•	Keras
•	Matplotlib
•	Streamline

IDEs and Programs
For the application several programs and IDEs are in use:

Frontend
•	VS Code
Backend
•	PyCharm
Model
•	Anaconda
•	Jupyter Notebook
•	PyCharm
•	Google Colab
2	Concept

2.1	Goal of the Provider

The goal of the provider is to provide a secure and efficient application that complies with the relevant laws. The application should primarily serve as a tool for the user to manage his e-commerce store.

2.2	Goal of the User

The user's goal is to upload products to the application efficiently and easily. Afterwards, the result is freely available for the user and can be further used.

2.3	Stakeholders and Personas

Stakeholder is anyone who has a website and at best can access the code of the website.

2.4	Software and Hardware Requirements of the Users
Hardware Requirements
● Processor: 1 Gigahertz or above
● RAM: 1 gigabyte (GB) (32-bit) or 2 GB (64-bit)
● Output Device: Screens of Monitor or a Laptop 
Software Requirements
● Operating system: Windows, Mac & Linux 
● Browser: Internet Explorer, Edge, Chrome, Firefox, Safari, Opera
● Server: Web Server 


3	Functional Requirements

Basic Features
•	the user can log in and out and leave his data
•	the user can delete his account or change data
•	the user can save his data
•	user can change website view and other settings
•	the user can create and upload code, images and others
•	the user can download or copy the data given back by the model


Extended Features
•	can share the application on social media
•	can write reviews and give voting
•	the user can connect his google-mail
•	the user can track his activities
•	the user gets notifications and updates
•	the user can see his account and status

4	Non-Functional Requirements

4.1	General Requirements

Loading time
Page speed
The page speed is based on the specifications of Google Lighthouse, the aim is to achieve a page speed of over 90 points according to the Google metrics.

Usability
The Design has to follow the 10 Usability Heuristics for User Interface Design by Nielsen and should be tested at the end by using eye tracking and usability testing.

Responsive Design
The design has to be responsive for all common devices such as smartphone, tablet, laptop and desktop. The focus of the web application is on laptop and desktop which means it follows “desktop first”.

4.2	Legal Requirements

Data Security
The system must comply with the German Data Protection Act.
Cookies
Google Analytics may also be used later on to track users, this needs to be considered at an early stage.

4.3	Technical Requirements

Conformity with other Browsers
One important thing is that the web application is conform with all kinds of standard browsers. Especially such as Chrome, Safari, Bing and Mozilla Firefox.

5	General Conditions

5.1	Timetable

The general processing period of the project is from 1.9.2022 to 31.1.2023, with a minimum of 40 hours of processing time each week.
5.2	Technical Requirements

To complete the project, it is necessary to have access to Google Colab and Jupyter Notebook.
As hardware it is recommended to have one laptop for working mobile and a tower computer to train the model.


5.3	Risk Analyses

Risk Table

5.3.1	Dependencies to other Frameworks, Packages…


5.4	Quality and Testing



6	Data situation



7	Definition of Done

Hier wird festgehalten, in welchem Umfang und zu welchem Preis Sie an Ihren Kunden wann und wo liefern sollen.
Witerhin wird hier spezifiziert, wann das Projekt als abgeschlossen gilt und wer definiert, ob die Qualität stimmt. Es sollte klar festgelegt werden, wer für die Abnahme verantwortlich ist.

8	Attachments

Alle weiteren Dokumente oder Zahlen und Fakten, die als Hintergrund zu dem Projekt dienen.


System Overview
Überarbeiten!


Frontend

In the following everything is collected what has to do with the frontend

Functional Requirements of the Frontend

•	User can create an account
•	User can delete his account
•	User can change his account information
•	User can see his account information
•	User can log in
>	CRUD in Database


Actual Frontend Design
 
Figure 3 Login Page
 
Figure 4 Upload Page
 
Figure 5 Result page

Figure 7 Account Setting Page


9	High-Fidelity Prototype Frontend

Link to Prototype: https://e2cxkf.axshare.com

10	Use Case Diagram

 
The user can easily upload his product and the system identifies to product. After this it creates the meta tags and saves the output, sends it back to the user and building/showing the knowledge graph to the user.

11	Class Diagram


12	Sequence Diagrams


Login Process
Description of the login process
The user has to decide if he wants to create an account or to login. For login he just needs his password and username/email. For later to deploy that you can click the function “forgot password”.


Registration Process

The User has to enter firstname, lastname, username,
password, mail. For later it is necessary to enter the address and his birthday. The goal is that the Form and build in functions of Flask prevent all input errors

13	Activity Diagram

Backend

In the following everything is collected what has to do with the Backend.
The backend is written in Flask.

Functional Requirements
•	Sending data to database
•	Retrieves data from database
•	Send data to filter that data would be cleaned


Das Backend wurde mittels Flask gestaltet. Grund hierfür war vor allem, dass Flask im Gegensatz zu Django wesentlich leichtgewichtiger ist und so der Performance entgegenkommt. 
Mit dem Backend ist eine SQL Lite Datenbank verbunden. Es werden nur die Anmeldedaten und Uploaddaten des Users gespeichert. Später muss die SQL Lite Datenbank ggf. gegen eine MySQL Datenbank getauscht werden.
Es ist dem User möglich sich anzumelden, sich zu registrieren, Änderungen an seinem Account vorzunehmen und seinen Account zu löschen. 


Database

In the following everything is collected what has to do with the Database.

14	Database Schema


Entity Relationship Diagram
First Concept not finished!



Data Pipeline

The user can upload his shop url than the webshop gets scraped, he can upload some text or html manually or upload an image of the product eg. of the webshop. Than there are two ways. In the first way the data gets store an is displayed on the website, on the other way the data gets stored for the model. 

 
Product Data

The Product has to have a specific dataset a specific saved attribute. While merging all datasets it´s necessary to declare the common and shared attribute.

Product
Brand, Category, Color, Description, Price, Title, Review, Price Currency, item Condition, Manufacturer, Aggregate Rating, Release Date, weight, width, size, logo, award

When the data is uploaded it comes in a preprocessed text. Now the task here is to identify all the essential properties in the text according to schema.org



First Test 
Loading up Fashion and detects the attributes!
Find Product Brand of fashion product in Uploaded text.


Extract Prices from Text
To extract prices from texts is very difficult. Especially because the OCR Model detects pounds as an E.
->Separate Price Currency
->Digits have to be separated from text


Model

In the following everything is collected what has to do with the ML-Model.

Binary Classification for Title Classification

Sequential Model
LSTM Model
BiLSTM Model



Algorithm To detect biggest Font

The general procedure is as follows:
To begin, the user uploads a screenshot of their product. This screenshot is extracted by OCR and the text is read out. These texts form the basis for the following extraction of the product attributes.
Extracting the product attributes
Since text is very difficult to classify, the OCR process already starts to distinguish the text components. The first step is to examine whether the input is a title or not, this follows a classical binary classification. The components that can be a title should be sorted out in advance and examined specifically. One possibility is to identify the largest and widest lettering on the image and save them as title candidates. The model for recognizing titles should then be applied specifically to this.
In the following the algorithm is shown, which recognizes the title candidates of images.

import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

reader = easyocr.Reader(['en'], gpu=False)

def preprocessing_image(image):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image

image = cv2.imread("test_images/test3.png")

image = preprocessing_image(image)

#to get the biggest rectangle
result_title = reader.readtext(image, paragraph = False, height_ths=0.5, width_ths=1)


#list of the rectangle values
height_list = []
divided_width = []

top_high_val = []
top_width_val = []

for index,detection in enumerate(result_title): 

    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    bottom_left = tuple(detection[0][3])

    image_rectangle = cv2.rectangle(image,(int(top_left[0]),int(top_left[1])),(int(bottom_right[0]),int(bottom_right[1])),(0,255,0),1)

    height_list.append(np.subtract(bottom_left[1],top_left[1]))

    width_sentence = np.subtract(bottom_right[0],bottom_left[0])

    len_sentence = len(detection[1])

    boldest_font = np.divide(len_sentence, width_sentence)

    divided_width.append(boldest_font)

#three highest values
highest_values = list(set(height_list))
highest_values = sorted(highest_values, reverse=True)[:5]

#three boldest font values
widthest_values = list(set(divided_width))
widthest_values = sorted(widthest_values, reverse=False)[:5]

#find indexes of widthest three values in divided_width list

for width in divided_width:
    if width in widthest_values:
        index_of_width = divided_width.index(width)
        top_width_val.append(result_title[index_of_width][1])

for height in highest_values:
    if height in highest_values:
        index_of_height = height_list.index(height)
        top_high_val.append(result_title[index_of_height][1])

title_candidates = list(set(top_width_val).intersection(top_high_val))

print(title_candidates)

plt.imshow(image_rectangle)
plt.show()
Data Preprocessing
def clean_data(data):
  
  data = data[['title','category','brand', "description"]]

  special_chars = ['~', ':', ",",".", "'", '+', '[', '\\', "&nbsp;", '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

  contractions = { 
"ain't": "am not / are not / is not / has not / have not",
"aren't": "are not / am not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had / he would",
"he'd've": "he would have",
"he'll": "he shall / he will",
"he'll've": "he shall have / he will have",
"he's": "he has / he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has / how is / how does",
"I'd": "I had / I would",
"I'd've": "I would have",
"I'll": "I shall / I will",
"I'll've": "I shall have / I will have",
"I'm": "I am",
"I've": "I have",
"isn't": "is not",
"it'd": "it had / it would",
"it'd've": "it would have",
"it'll": "it shall / it will",
"it'll've": "it shall have / it will have",
"it's": "it has / it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had / she would",
"she'd've": "she would have",
"she'll": "she shall / she will",
"she'll've": "she shall have / she will have",
"she's": "she has / she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as / so is",
"that'd": "that would / that had",
"that'd've": "that would have",
"that's": "that has / that is",
"there'd": "there had / there would",
"there'd've": "there would have",
"there's": "there has / there is",
"they'd": "they had / they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they shall have / they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had / we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what shall / what will",
"what'll've": "what shall have / what will have",
"what're": "what are",
"what's": "what has / what is",
"what've": "what have",
"when's": "when has / when is",
"when've": "when have",
"where'd": "where did",
"where's": "where has / where is",
"where've": "where have",
"who'll": "who shall / who will",
"who'll've": "who shall have / who will have",
"who's": "who has / who is",
"who've": "who have",
"why's": "why has / why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had / you would",
"you'd've": "you would have",
"you'll": "you shall / you will",
"you'll've": "you shall have / you will have",
"you're": "you are",
"you've": "you have"
}

  # Remove special chars and elements only containing of digits
  clean_title = data.apply(lambda x: str(x["title"]).isdigit() == False and str(x["title"]) not in special_chars,axis=1)
  clean_category = data.apply(lambda x: str(x["category"]).isdigit() == False and str(x["category"]) not in special_chars,axis=1)
  clean_brand = data.apply(lambda x: str(x["brand"]).isdigit() == False and str(x["brand"]) not in special_chars,axis=1)
  clean_description = data.apply(lambda x: str(x["description"]).isdigit() == False and str(x["description"]) not in special_chars,axis=1)
  # Keep only titles with less than 30 words
  shorten_title = data.apply(lambda x: len(x["title"].split(' ')) < 30,axis=1)
  # Keep only descriptions with less than 300 words
  shorten_discription= data.apply(lambda x: len(x["description"].split(' ')) < 300, axis=1)
  # Remove unformatted rows
  filled_data = data.fillna('')

  is_html = filled_data.title.str.contains('getTime')

   # Replace entity html codes : 
  
  to_replace = {
      '&quot;': '"',
      '&copy;': '',
      '&reg;' : '',
      '&amp;': '&'
  }

  #replace html tags
  filled_data = filled_data.replace(to_replace)

  #expand concrations in text
  removed_contractions_data = filled_data.replace(contractions)

  # Deduplicate 
  df_clean = removed_contractions_data.drop_duplicates(subset=['title', "category", "brand", "description"], keep='first')

  #remove empty lists
  df_clean[df_clean.astype(str)[["title", "category", "brand", "description"]] != '[]']

  df_clean = df_clean[~is_html][shorten_title][shorten_discription][clean_title][clean_category][clean_brand][clean_description]

  #lower data
  df_clean["title"] = df_clean["title"].str.lower()
  df_clean["category"] = df_clean["category"].str.lower()
  df_clean["brand"] = df_clean["brand"].str.lower()
  df_clean["description"] = df_clean["description"].str.lower()

  #call function stopwords from NLTK
  stop_words = set(stopwords.words('english'))
  stop_words.add('subject')
  #to remove http links
  stop_words.add('http')

  #remove the stopwords from column
  #df_clean["title"] = df_clean["title"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
  df_clean["category"] = df_clean["category"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
  #df_clean["brand"] = df_clean["brand"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
  df_clean["description"] = df_clean["description"].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

  #Lemma data
  lemmatizer = WordNetLemmatizer()
  #Lemmatize columns data
  #df_clean["title"] = df_clean["title"].apply(lambda word: lemmatizer.lemmatize(word, pos='v'))
  df_clean["category"] = df_clean["category"].apply(lambda word: lemmatizer.lemmatize(word, pos='v'))
  #df_clean["brand"] = df_clean["brand"].apply(lambda word: lemmatizer.lemmatize(word, pos='v'))
  df_clean["description"] = df_clean["description"].apply(lambda word: lemmatizer.lemmatize(word, pos='v'))

  df_clean['title'] = df_clean['title'].str.replace(r'<[^<>]*>', '', regex=True)
  df_clean['category'] = df_clean['category'].str.replace(r'<[^<>]*>', '', regex=True)
  df_clean['brand'] = df_clean['brand'].str.replace(r'<[^<>]*>', '', regex=True)
  df_clean['description'] = df_clean['description'].str.replace(r'<[^<>]*>', '', regex=True)

  return df_clean

Datenlage
Für den Datensatz wurden verschiedene im Internet freizugängliche Datensätze verwendet und zusammengeführt. Das Bereinigen der Daten und das Formatieren beanspruchte lange Zeit. Dabei sind verschiedene Datensätze entstanden. Wichtig zu erwähnen ist hierbei, dass die hier beschriebenen Datensätze vor allem darauf abzielen den Titel eines Produktes zu klassifizieren. Weitere später entstehende Datensätze werden noch aufgeführt. 
Die Begründung mehrere verschiedene Datensätze zu erstellen liegt darin begründet, dass die verschiedenen Datensätze auch verschiedene algorithmischen Strukturen folgen. So gibt es einen Datensatz, welcher vor allem für die binäre Klassifizierung zwischen Description und Title eingesetzt wird und aber auch Datensätze, welche für multiclass Klassifizierung eingesetzt werden.
Im Allgemeinen ist der erste Versuch der, dass One Vs. Rest verwendet wird. Das bedeutet, dass beim Input der Daten zuerst überprüft wird, ob es sich um den Titel handelt oder eben nicht. Es ist also eine schlichte Binäre Klassifizierung. Wurde der Titel mit unter Zuhilfenahme der Extraktion des größten Schriftzugs aus dem Bild vollführt ist es der nächste Schritt den Brand innerhalb des Titels oder aber auch in den anderen Bestandteilen des Inputs zu klassifizieren. Wurden Titel und Brand entdeckt werden diese markiert und mittels eines Ausschlussverfahrens werden die folgenden Attribute erschlossen. 
Preise und Farbnahmen, sowie Größenangaben werden versucht mittels eines Dictionaries zu lösen. Auch hier bleibt noch zu erörtern inwiefern das Zielführend ist.
Durch das Sammeln von Daten konnten vor allem 4 Attribute extrahiert werden. Titel des Produkts, Category des Produkts, Brand des Produkts und Beschreibung des Produkts. Das Vorgehen bzw. der erste Versuchsaufbau läuft derart ab, dass ein Datensatz mit diesen vier Merkmalen erstellt wird.
Insgesamt nach dem Preprocessen der Daten sind 13172462 Produkte (Stand 28.09.2022) mit den Attributen Titel, Category, Brand und Description vorhanden. 

Preprocessing der Daten
Wichtiger Bestandteil beim Arbeiten mit Textdaten ist das NLP. Als erster Schritt wurden die Einträge des Datensatzen in lowercase gesetzt. Anschließend spezielle Zeichen, wie Add Symbole etc. entfernt. Zu Beginn wurden vorrangig Description und Category bearbeitet, da Brand und Titel oft Eigennamen beinhalten und nicht zu stark verändert werden sollten. Brand und Title müssen später vielleicht dennoch noch angepasst werden. Dies bleibt noch zu klären. 
So wurde das Lemmatizieren nur auf die Produktbeschreibung und die Category angewandt. Auch wurden HTML Tags etc. zudem entfernt. Die länge der Beschreibung überschreitet hierbei nicht die Anzahl von 300 Buchstaben und die Länge des Titels nicht die 30.
Title Classification
Die Phänomenologie eines Produkt Titels ist sehr verschieden zu anderen Texten. Ein Titel ist meist kürzer als ein Satz, hat ein undefiniertes Ende und ist grammatikalisch oft verschieden aufgebaut. Daher muss ein Produkt Titel bzw. dessen Klassifizierung anders betrachtet werden als bei gängiger Textklassifizierung. Laut diversen Forschungen* ist das Entfernen von Stopwords und die Lemmatizierung bzw. das Stemming für die Klassifizierung kontraproduktiv. Dementsprechend sollten die Daten möglichst nicht zu aufwendig preprocessed werden. 
Des Weiteren hat sich gezeigt, dass das Verwenden von Bigrams die Klassifizierung fördert. Auch das Verwenden eines 




Title vs Description Binary Text Classification

Plotting the Data
 

In der obigen Grafik erkennt man die Verteilung im Datensatz zwischen Description (0) und Title. Da diese beiden Klassen noch stark voneinander abweichen, vor allem da in Realität mehr Descriptions existieren als Title müssen diese beiden Klassen noch einander angepasst werden. Es wird jeweils under and oversampling angewandt.

 
Obige Grafik mit hinzugefügten Brands in den Datensatz.

 
Wie zu sehen ist umfasst der Datensatz für title vs description bereits 5781026 verschiedene Tokens.
Update
 
Im finalen Datensatz sind über 3.71 Mio einzelne Tokens vorhanden.
Oben zu sehen, die 25 häufigsten Wörter, wobei dies in Anbetracht der Größe des Datensatzes nicht sonderlich sinnvoll ist.
Für die erste Binäre Klassifizierung wurden jeweils zwei Kolonnen des Dataframes extrahiert wobei jede Kolonne, also title und description jeweils ein Target zugewiesen bekommen haben. Was bedeutet, dass Title und description gleich X darstellt und das Target die Y Komponente. Im Falle von title ist Y gleich 1 und bei description gleich 0. Insgesamt umfasst der Datensatz an die 22 Mio. Zeilen und ist 3GB groß. 
Nach dem Zusammenführen und cleanen der Daten ist es Aufgabe das Model mit diesen Daten zu trainieren. Der Verlauf des Trainings wird hier dokumentiert:

Das Model wird über die Plattform Google Colab trainiert.
Google Colab Tricks
Avoid Google Colab from Disconnecting:
function ClickConnect(){
console.log("Working"); 
document.querySelector("colab-toolbar-button#connect").click() 
}setInterval(ClickConnect,60000)

CODE um RAM zu erhöhen
mem = []
while True:
mem.append(' ' * 10**6)

Deep Learning Model

 
Figure 8 DL-Model des ersten Testlaufs
    

Training Logistic Regression
TfidfVectorizer vs CountVectorizer
Beim Vektorizieren des Textes gibt es diverse Ansätze im vorab werden spezifisch TfidfVectorizer und CountVectorizer. Word2Vec etc. werden anschließend näher betrachtet. Im Trainingsverlauf zeigt sich, dass TfidfVectorizer bessere Accuracy erreicht als CountVectorizer

TfidVectorizer less memory usage
Np.float32 vs np.float64

1.Training LR Model
Training mit LR lief sehr gut bei vier eingaben konnte das Model immer richtig zwischen Titel und Description
Max_features = 1500 weiter erhöhen!
 

Confusion Matrix 
 

Eingabe eines ganzen Produkts

 

 
Class	Precision	Recall	F1-Score	Support
0	0.96	0.82	0.88	
1	0.91	0.98	0.94	
accuracy	0.92			
Macro avg	0.93	0.90	0.91	
Weighted avg	0.93	0.92	0.92	

2. Training LR Model
LR with Tfid Vectorizer and max_features=3000 and bigrams in Tfid Vectorizer

Class	Precision	Recall	F1-Score	Support
0	0.93	0.64	0.76	
1	0.83	0.97	0.89	
accuracy	0.85			
Macro avg	0.88	0.81	0.82	
Weighted avg	0.86	0.85	0.84	

3.Training LR Model
TfidVectorizer, max_features=3000, keine Bigrams
Class	Precision	Recall	F1-Score	Support
0	0.96	0.87	0.91	
1	0.93	0.98	0.95	
accuracy	0.94			
Macro avg	0.94	0.92	0.93	
Weighted avg	0.94	0.94	0.94	

Training 4
Tfid Vectorizer, max_features=4500 as np.float 32 as dtype

Class	Precision	Recall	F1-Score	Support
0	0.52	0.87	0.65	
1	0.88	0.54	0.67	
accuracy	0.66			
Macro avg	0.70	0.70	0.66	
Weighted avg	0.75	0.66	0.66	

Training 5 Logistic Regression
Tfid Vectorizer, max_features=4500 as np.float 64 as dtype

Class	Precision	Recall	F1-Score	Support
0	0.52	0.87	0.65	
1	0.88	0.54	0.67	
accuracy	0.66			
Macro avg	0.70	0.70	0.66	
Weighted avg	0.75	0.66	0.66	

Training 6 Logistic Regression
Tfid Vectorizer, max_features=2000 as np.float 64 as dtype

Training 7
Tfid Vectorizer, max_features=1500 as np.float 64 as dtype, solver liblinear

Class	Precision	Recall	F1-Score	Support
0	0.64	0.85	0.73	
1	0.90	0.73	0.81	
accuracy	0.77			
Macro avg	0.77	0.79	0.77	
Weighted avg	0.80	0.77	0.78	

Training 8
Tfid Vectorizer, max_features=2500 as np.float 64 as dtype, solver liblinear

Class	Precision	Recall	F1-Score	Support
0	0.68	0.85	0.75	
1	0.90	0.77	0.83	
accuracy	0.80			
Macro avg	0.79	0.81	0.79	
Weighted avg	0.82	0.80	0.80	

Training 9
Tfid Vectorizer, max_features=3000 as np.float 64 as dtype, solver liblinear
 
Training 10
Tfid Vectorizer, max_features=3500 as np.float 64 as dtype, solver liblinear

Training 11
Tfid Vectorizer, mf_df= 5, as np.float 64 as dtype, solver liblinear, sublinear=True

Class	Precision	Recall	F1-Score	Support
0	0.97	0.89	0.93	
1	0.94	0.98	0.96	
accuracy	0.95			
Macro avg	0.95	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

Table Binary Classification Title vs. Description Logistic Regression
Traingsnummer	Solver	Vectorizer	Features	n-gram	Score
Training 1	liblinear	CV-Vec	1500	uni	92%
Training 2	liblinear	Tfid-Vec	3000	bi	85%
Training 3	liblinear	Tfid-Vec	3000	uni	93%
Training 4	liblinear	Tfid-Vec	4500	uni	65%
Training 5	liblinear	Tfid-Vec	4500	uni	66%
Training 6	liblinear	Tfid-Vec	2000	uni	85%
Training 7	liblinear	Tfid-Vec	1500	uni	77%
Training 8	liblinear	Tfid-Vec	2500	uni	80%
Training 9	liblinear	Tfid-Vec	3000	uni	73
Training 10	liblinear	Tfid-Vec	3500	uni	71%
Training 11	liblinear	Tfid-Vec	Mf_df=5	uni	95%


Logistic Regression with undersampled data

1.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=5, unigram

 
Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	


2.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=5, unigram
Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

3.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=5, n_gram = (1,2),128Mb Config (funktioniert nicht)


4.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=6, n_gram = (1,1)
 

Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

5.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=4, n_gram = (1,1)
 

Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

6.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=7, n_gram = (1,1)
 

Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

7.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=3, n_gram = (1,1)
 
Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

8.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=10, n_gram = (1,1)
 
Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

9.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=1, n_gram = (1,1)
 
Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.96	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.94	

10.Training
Logistic Regression with undersampled Data, liblinear, tfid-vec, mf_df=20, n_gram = (1,1)
 
Class	Precision	Recall	F1-Score	Support
0	0.94	0.91	0.92	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.94	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

Logistic Regression Undersampled Data
Traingsnummer	Solver	Vectorizer	Features	n-gram	Score
Training 1	liblinear	Tfid-Vec	Mf_df=5	(1,1)	94,6%
Training 2	liblinear	Tfid-Vec	Mf_df=5	(1,1)	94,5%
Training 3	liblinear	Tfid-Vec	Mf_df=5	(1,2)	X
Training 4	liblinear	Tfid-Vec	Mf_df=6	(1,1)	94,5%
Training 5	liblinear	Tfid-Vec	Mf_df=4	(1,1)	94,5%
Training 6	liblinear	Tfid-Vec	Mf_df=7	(1,1)	94,5%
Training 7	liblinear	Tfid-Vec	Mf_df=3	(1,1)	94,5%
Training 8	liblinear	Tfid-Vec	Mf_df=1	(1,1)	94,5%
Training 9	liblinear	Tfid-Vec	Mf_df=10	(1,1)	94,5%
Training 10	liblinear	Tfid-Vec	Mf_df=20	(1,1)	94,5%

Notice:
•	Sublinear= False erbringt keinen großen Unterschied

Logistic Regression with oversampled data

1.Training
Logistic Regression with oversampled Data, liblinear, tfid-vec, mf_df=5, unigram

Class	Precision	Recall	F1-Score	Support
0	0.95	0.90	0.93	
1	0.95	0.97	0.96	
accuracy	0.95			
Macro avg	0.95	0.94	0.94	
Weighted avg	0.95	0.95	0.95	

Wie man sieht gibt es kaum eine Veränderung gegenüber dem Undersamplen, doch verdoppelt sich die Trainingszeit.

Logistic Regression with brand + description data

Class	Precision	Recall	F1-Score	Support
0	0.92	0.90	0.91	
1	0.93	0.94	0.94	
accuracy	0.93			
Macro avg	0.92	0.92	0.92	
Weighted avg	0.93	0.93	0.93	
 
Es sieht nach einem Rückgang in der Precision aus, wenn zusätzlich Brand Daten zum Datensatz hinzugefügt werden. Es muss aber auch überprüft werden, ob die Funktion max_features nicht auch Probleme verursacht, da Brandnamen meist nur einmal auftreten und so wieder entfernt werden könnten. 

Logistic Regression Title Classification with Word2Vec

Logistic Regression Title Classification with Glove

Support Vector Machine Binary Text Classification
Table Binary Classification Title vs. Description SVM

Traingsnummer	Solver	Vectorizer	Features	n-gram	Score
Training 1	linear	Tfid-Vec	mf_df=5	uni	
Training 2					
Training 3					
Training 4					
Training 5					
Training 6					
Training 7					
Training 8					
Training 9					
Training 10					
Training 11					

Split letters from numbers in title data
As a variant in one dataset there were numbers and letters separated from each other. It has to turn out by testing if it will work out. Some problems can occurrent for example by a title like “S8 Android Phone”, because it will turn to “S 8 Android Phone”.

N-Gram Testing with Logistic Regression
n-gram mit n=5

Es wird überprüft welche n-gram Anzahl die höchste Score besitzt.

N-Gram Logistic Regression
Traingsnummer	Solver	Vectorizer	Features	n-gram	Score
Training 1	liblinear	Tfid-Vec	mf_df=5	(1,1)	94,8%
Training 2	liblinear	Tfid-Vec	mf_df=5	(1,2)	
Training 3	liblinear	Tfid-Vec	mf_df=5	(1,3)	
Training 4	liblinear	Tfid-Vec	mf_df=5	(1,4)	
Training 5	liblinear	Tfid-Vec	mf_df=5	(1,5)	
Training 6	liblinear	Tfid-Vec	mf_df=5	(2,2)	
Training 7					

Multinomial Naive Bayes Title Classification
Training 1

Class	Precision	Recall	F1-Score	Support
0	0.87	0.87	0.87	
1	0.92	0.92	0.92	
accuracy	0.90			
Macro avg	0.89	0.89	0.89	
Weighted avg	0.90	0.90	0.90	

  
NB hat zwar schlechteren Score, aber erkennt den Titel eindeutig.

Training 2   
Brand + Description Data
Class	Precision	Recall	F1-Score	Support
0	0.94	0.82	0.88	
1	0.91	0.97	0.94	
accuracy	0.92			
Macro avg	0.92	0.90	0.91	
Weighted avg	0.92	0.92	0.92	

Multiclass Algorithm Title Classification
 
In obiger Grafik erkennt man die Aufteilung der imbalanced classes im Datensatz. Die Anzahl der Titel ist dementsprechend wesentlich höher als die restlichen Kategorien. Im Normalfall können derartig starke Abweichungen im Datensatz zu Problemen führen und Klassen, die weniger Datensätze umfassen als Outlier behandeln. Die Daten müssen also noch gebalanced werden. Im weiteren wird erörtert in wie fern Undersampling oder Oversampling zu besseren Ergebnisses führen kann.
Der Datensatz verfügt dabei über 21,5 Mio. Zeilen, welche bereits bereinigt und frei von Null-Werten sind.


Momentan besitzt der Datensatz 4 Klassen, es sollen aber noch einige hinzugefügt werden, so z.B. Preis, Sku, ASIN, Reviews etc.
Classes 
Title, Brand, Description, Category
Data
Target
0,1,2,3

Multiclass Training Logistic Regression
Traingsnummer	Solver	Vectorizer	Features	n-gram	Score
Training 1	saga	CV-Vec	1500	uni	80%
Training 2	saga	Tfid-Vec	1500	uni	75%
Training 3	saga	Tfid-Vec	min_df=5	uni	94%
Training 4		Tfid-Vec		uni	
Training 5					
Training 6					
Training 7					
Training 8					
Training 9					
Training 10					
Training 12					
					
Multiclass Training 1 Logistic Regression
Max_features=1500, Count Vectorizer, 

Class	Precision	Recall	F1-Score	Support
0	0.98	0.29	0.45	
1	0.96	0.95	0.96	
2	0.81	0.77	0.79	
3	0.78	0.89	0.83	
accuracy	0.81			
Macro avg	0.88	0.73	0.76	
Weighted avg	0.82	0.81	0.79	

Multiclass Training 2 Logistic Regression
Max_features=1500, TfidVectorizer

Multiclass Training 2 Logistic Regression
Mf_df=5, TfidVectorizer

Multiclass Training 3 Logistic Regression
Mf_df=5, TfidVectorizer, saga solver

 
KNN Title Classification
Training 1
n=3
Class	Precision	Recall	F1-Score	Support
0				
1				
accuracy				
Macro avg				
Weighted avg				


Decision Tree Title Classification

1.Training Tfid-Vectorizer, mf_df=5, undersampled


Time and Space Complexity of the ML-Algorithms

Time Complexity
1.	Quadratic Time Complexity
2.	Linear Time Complexity
3.	Fractional Time Complexity
4.	Exponential Time Complexity

KNN Algorithm

Brute Force KNN
O(knd), where k = number nearest neighbours, n = datapoints in data,
d=dimensions

kd Tree KNN
O(n d log(n))where k = number nearest neighbours, n = datapoints in data,
d=dimensions

Category Classification
With the models which separate Brand, Title and Description is it the goal to detect the Category of the Product. Therefore the models extract title, brand and description and they are used as input for the category classification model.


Three Attribute Classification


Oversample Brand and undersample description

1.Training Multinomial Multiclass

              precision    recall  f1-score   support

         0.0       0.87      0.78      0.82    499074
         1.0       0.57      0.95      0.71   1613339
         2.0       0.95      0.61      0.74   2846690

    accuracy                           0.73   4959103
   macro avg       0.80      0.78      0.76   4959103
weighted avg       0.82      0.73      0.74   4959103

 

Werden Brand , Title und description im undersampling zusammengefügt, ist das Ergebnis recht interessant, da zwar titel nicht eindeutig erkannt werden, aber wenn sie erkannt werden dann recht sicher!

2.Training Logistic Regression

Datensatz Brand, Title, Description undersampled Title

 
Category Classification

Important Papers 

https://arxiv.org/pdf/2109.01084.pdf

https://www.csie.ntu.edu.tw/~cjlin/papers/title.pdf

