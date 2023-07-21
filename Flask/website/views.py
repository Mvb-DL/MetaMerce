from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from .models import ExtractedProduct, Upload
from . import db
import requests, base64, csv, justext, json, urllib.request
from .controllers.user_controller import UserController
from .controllers.company_controller import CompanyController
from .controllers.api_controller import ApiController
from .controllers.product_controller import ProductController
from .controllers.data_controller import DataController
from .ml_models import *

UC = UserController()
CC = CompanyController()
PC = ProductController()
AC = ApiController()
DC = DataController()

#defining the name of the blueprint
views = Blueprint('views', __name__)


#route to the landingpage
@views.route("/", methods=["GET", "POST"])
def landingpage():
    number_products = PC.count_products()
    return render_template("index.html", user=current_user, number_products=number_products)


#the function to display the upload of the user
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    number_products = PC.count_products()
    user_product_list = PC.get_products_user()

    user_categories = []

    for p in user_product_list:
        user_categories.append(p.category)

    count_user_categories = [[x, user_categories.count(x)] for x in set(user_categories)]

    counting_products = []
    user_products = []

    for count in count_user_categories:
        counting_products.append(count[1])

    for product in count_user_categories:
        user_products.append(product[0])

    return render_template("home.html", user=current_user, number_products=number_products, user_categories=user_products, counting_products=counting_products)



#The function to display the account of the user
@views.route('/account', methods=["Get",'POST'])
def account():

        return render_template("account.html", user=current_user, users=UC.get_user(), user_company=CC.get_user_company(), number_products=PC.count_products())


#deletes the account of the User
@views.route('/delete_account', methods=["GET",'POST'])
def delete_account():

        UC.delete_user()
        flash("Deleting Account was successful!", category="success")
        return redirect(url_for('auth.logout'))
    

#Deletes the upload of the User
@views.route('/delete-upload', methods=['POST'])
def delete_upload():
    upload = json.loads(request.data)
    uploadId = upload['uploadId']
    upload = Upload.query.get(uploadId)
    if upload:
        if upload.user_id == current_user.id:
            db.session.delete(upload)
            db.session.commit()

    return jsonify({})


#funciton to delete a company
#it´s connected with a js funciton to fetch the data
@views.route('/delete_company', methods=['POST'])
def delete_company():

    #from the js function it gets the information which company to delete
    company_id = request.get_json()
    CC.delete_user_company(company_id)

    return render_template("account.html", user=current_user)


#function to delete a product
#it´s connected with a js funciton to fetch the data
@views.route('/delete_product', methods=['POST'])
def delete_product():

    #from the js function it gets the information which product to delete
    product_id = request.get_json()
    PC.delete_user_product(product_id)

    #after deleting it updates the number of products again
    
    return render_template("company_profile.html", user=current_user, number_products=PC.count_products())


#this function gets called when the user goes on the company profile site if there is no registered company existing the user gets routed to sign up for a company profile
@views.route('/company_profile', methods=['GET', 'POST'])
def company_profile():

    #if no company exists the user gets routed to sign up a new company
    exist_company = CC.check_user_company()

    if exist_company is True:
        return redirect(url_for('auth.sign_up_company_profile'))

    category_names = []

    extracted_product = PC.get_products_user()

    for e in extracted_product:
        category_names.append(e.category)

    category_names = list(set(category_names))

    return render_template("company_profile.html", user=current_user, 
    category_names=category_names, number_products=PC.count_products(), user_company=CC.get_user_company(),
    extracted_product=extracted_product, user_company_id=CC.get_belonging_company())



#there is a feature to export the knowledge graph into a excel file
@views.route('/export_knowledge_graph', methods=['POST'])
def export_knowledge_graph():

    extracted_product = PC.get_products_user()

    with open("C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/static/uploads/knowledge_graph.csv", "w", newline="") as csvfile:
        
        csv_writer = csv.writer(csvfile, delimiter=",")
        csv_writer.writerow(["Title", "Description", "Brand", "Category", "Highest Price", "Lowest Price", "Prices", "Currency", "Country", "Meta Tag Code", "Filename"])

        for product in extracted_product:
            csv_writer.writerow([product.title, product.description, product.brand, product.category, product.high_price, product.low_price,
            product.price, product.currency, product.country, product.meta_tag_code_json_ld, product.filename])
        
    return send_file("C:/Users/mario.vonbassen/Desktop/MetaMerce/Flask/website/static/uploads/knowledge_graph.csv", mimetype="text/csv", as_attachment=True)




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#TODO
#Scraper for HTML
#its possible for the user to put in it´s website url and the website gets scraped. It´s to classify the extracted text
@views.route('/html_scraper', methods=['POST'])
def html_scraper():
    
    html_without_boilerplate = []
    
    scrape_url = request.form.get("html_scraper_input")

    if len(scrape_url) < 1:
        flash("Put in a valid url please!", category="error")
        return redirect(url_for('views.home'))

    scrape_page = requests.get(scrape_url)

    paragraphs = justext.justext(scrape_page.content, justext.get_stoplist("English"))

    for paragraph in paragraphs:

        if not paragraph.is_boilerplate:

            html_without_boilerplate.append(paragraph.text)
        else:

            html_without_boilerplate.append(paragraph.text)

    #preprocess text and than store it in file
    #preprocessed_text = text_preprocesser(html_without_boilerplate)

    return render_template("home.html", user=current_user, preprocessed_text=html_without_boilerplate)



#this funtion route the user to the api
@views.route("/root_API")
@login_required
def root_API():

    #if there exist an API profile the user gets directly routed to the API
    #if there is no Profile existing the user gets routed to a new funtion to sign up his new profile
    exist_api_profile = AC.check_api_profile()

    if exist_api_profile is True:
        return redirect(url_for('auth.sign_up_api_profile'))


    application_domain = AC.get_api_user_domain()


    if AC.api_connection_test(application_domain):

        posts = AC.get_posts(application_domain)
        pages = AC.get_pages(application_domain)

        posts_and_pages = posts + pages

        user_products = PC.get_products_user()
    
        return render_template("api.html", user=current_user, user_products=user_products, posts_and_pages=posts_and_pages)

    elif AC.api_connection_test(application_domain) is False:
        flash("Cannot build a connection to the API!", category="error")

    return redirect(url_for('auth.sign_up_api_profile'))


#build up the API for Meta Merce
@views.route("/API", methods=['POST'])
@login_required
def API():


    #this function gets the product id and finds the necessary product in the database
    def api_data():
    
        def get_product_meta_tag(product_id):

          user_product = ExtractedProduct.query.filter(ExtractedProduct.id == product_id).first()

          product_api_data = user_product.meta_tag_code_json_ld

          return product_api_data

        #gets the input of the user from the frontened 
        product_id = request.form.get("product_id")

        #thats the id of the post of the wordpress site
        post_data = request.form.get("wp_id")

        #the wp_id contains the id and which type of site it is a post or a page therefore it´s splitted up    
        post_data = post_data.split()

        post_id = post_data[0]

        wp_type = post_data[1]

        meta_tag_data = get_product_meta_tag(product_id)

        return meta_tag_data, post_id, wp_type


    meta_tag_data, post_id, wp_type = api_data()

    wordpress_username, application_password, application_domain = AC.get_api_user()

    meta_tag_data = AC.format_json(meta_tag_data)

    url, header = AC.auth_connection_api(wordpress_username, application_password, application_domain)

    #that is the post which is send to the Wp API
    post = {
        "charset" : "utf-8",
        "content": meta_tag_data,
        "status": "publish",
        "content-type": "application/ld+json"
    }

    #the wordpress API has an own link for posts and an own link for pages
    #depending on the wp_type it builds up the necessary surfix for the url
    def build_surfix(wp_type):

        if wp_type == "Post":
            url_surfix = "/posts/"
            return url_surfix

        if wp_type == "Page":
            url_surfix = "/pages/"
            return url_surfix

    url_surfix = build_surfix(wp_type)

    #send the post to wordpress in form of a put request
    r = requests.put(url + url_surfix + post_id, headers=header, json=post)

    return redirect(url_for('views.root_API', user=current_user))
    


@views.route('/extract_image', methods=['GET', 'POST'])
def extract_image():

    filename = request.args['filename']

    product_text, specified_word_list, base64_image = ocr_model(filename, title_length=2)
                
    #adds to base64 image the necessary tag
    base64_image = "data:image/jpeg;base64," + base64_image

    title, description = title_extraction(specified_word_list)

    brands = brand_extraction(title)

    category = category_extraction(title)

    prices, currency, imagetext_two, low_price, high_price = price_extraction(filename)

    countries = country_extraction(product_text, imagetext_two)

    new_product = PC.create_product(description=DC.prepare_datatype(description),
                    price=DC.prepare_datatype(prices), low_price=str(low_price),
                    high_price=str(high_price), title=DC.prepare_datatype(title),
                    brand=DC.prepare_datatype(brands), currency=currency,
                    category=DC.prepare_datatype(category), country=DC.prepare_datatype(countries),
                    filename=DC.prepare_datatype(filename), imagetext=DC.prepare_datatype(product_text),
                    belonging_company=CC.get_belonging_company())

    imagetext = json.dumps(product_text)

    return render_template("image_ml_model.html",
        user=current_user, 
        extracted_product=new_product,
        user_company=CC.get_current_user_company(),
        base64_image=base64_image,
        imagetext=imagetext)
