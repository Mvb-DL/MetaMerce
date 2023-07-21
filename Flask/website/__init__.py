from flask import Flask, redirect, url_for, request, flash
from .database import db, db_name
from flask_login import LoginManager
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit
from .controllers.data_controller import DataController
from .controllers.product_controller import ProductController
from .controllers.company_controller import CompanyController
from os import path
import os, json
from .ml_models import *

from .models import User

DC = DataController()
PC = ProductController()
CC = CompanyController()


def create_app():

    async_mode = None
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sbaukbdlaukbdsadasds'
    socketio = SocketIO(app, async_mode=async_mode)

    #calls sqllite
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    UPLOAD_FOLDER = 'website/static/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', "html", "htm"}

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    #max size of an uploaded image
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    #import the blueprints
    from .views import views
    from .auth import auth

    #we register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    #creates the database
    create_database(app)

    #checks the datatype of the uploaded content
    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    #gets the json data to find the correct product in the database
    def get_extracted_product(product_data):

          for key, value in product_data.items():

            if key == "product_id":

                extracted_product = PC.get_exact_product(value)
                return extracted_product
 

    #upload images as file
    @app.route('/upload_file', methods=["GET", 'POST'])
    def upload_file():
        
        #if request.method == 'POST':

                if CC.check_user_company():
                    return redirect(url_for('auth.sign_up_company_profile'))

                if 'file' not in request.files:
                    flash('No file part', category="error")
                    return redirect(request.url)

                files = request.files.getlist('file')

                for file in files:

                    if file.filename == '':
                        flash('No selected file', category="error")
                        return redirect(url_for("views.home"))

                    if file and allowed_file(file.filename):

                        filename = secure_filename(file.filename)

                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                        return redirect(url_for("views.extract_image", filename=filename))


#to dispaly the image
    @app.route('/display/<filename>')
    def display_image(filename):
        return redirect(url_for('static', filename='uploads/' + filename), code=301)



    #gets data input from frontend to change product data without reloading website new
    @socketio.on('my_event', namespace='/product_edit_socket')
    def update_extracted_product(json):

            extracted_product = get_extracted_product(json)

            for key, value in json.items():

                if len(str(value)) > 0:

                    extracted_product.key = value
                    db.session.commit()
                    emit(f"{key}_update", extracted_product.key)



    #TODO
    #the user can add new meta code data without reloading the site new
    @socketio.on('my_event_2', namespace='/add_product_meta_code')
    def add_product_meta_code(json):

        try:

            for key, value in json.items():

                """

                if key == "meta_key":

                  added_meta_tag = "," + '"' + value + '"' + ":" + '"'

                  if key == "meta_value":

                    added_meta_tag = added_meta_tag + value + '"'

                    print(added_meta_tag)

                    emit("added_meta_tag", added_meta_tag)
                """
        except:
            flash("Socket 2 has crashed", category="error")



    #text can be saved without reloading whole page new
    @socketio.on('my_event_3', namespace='/save_meta_text')
    def save_meta_text(json):

            extracted_product = get_extracted_product(json)

            for key, value in json.items():

                if key == "meta_text":

                  extracted_product.meta_tag_code = value
                  db.session.commit()


    #in the home site the user can add code to transform it to meta code
    @socketio.on('my_event_4', namespace='/add_product_meta_code')
    def add_product_meta_code(json):
      
            extracted_product = get_extracted_product(json)

            for key, value in json.items():

                    extracted_product.key = value
                    db.session.commit()


#!!!!!!!!!!!!!!!!
#TODO eleganter lösen
    @socketio.on('my_event_5', namespace='/add_manual_product_input')
    def add_manual_product_input(json):

          value_list = []

          for key, value in json.items():

                value_list.append(value)

          new_product = PC.create_product(title=value_list[0], description=value_list[1],
                            brand= value_list[2], low_price=value_list[3], high_price=value_list[4],
                            currency=value_list[5],country=value_list[6], category=value_list[7],                    
                            belonging_company=CC.get_belonging_company())


#!!!!!!!!!!!!!!!!!!!!!!!!!!
#TODO eleganter lösen
          def count_products():

            user_products = PC.get_products_user()

            user_categories = []

            for p in user_products:
              user_categories.append(p.category)

            count_user_categories = [[x, user_categories.count(x)] for x in set(user_categories)]

            counting_products = []
            user_products = []
  
            for count in count_user_categories:
                counting_products.append(count[1])
  
            for product in count_user_categories:
                user_products.append(product[0])
              
            return user_products, counting_products
            
            
          user_categories, counting_products = count_products()

          emit("manual_title", new_product.title)
          emit("manual_description", new_product.description)
          emit("manual_brand", new_product.brand)
          emit("manual_low_price", new_product.low_price)
          emit("manual_high_price", new_product.high_price)
          emit("manual_currency", new_product.currency)
          emit("manual_country", new_product.country)
          emit("manual_category", new_product.category)
          emit("user_categories", user_categories)
          emit("counting_products", counting_products)


    #handles the login for the user
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app


#function that creates the database
def create_database(app):
    with app.app_context():
        if not path.exists('website/' + db_name):
            db.create_all()
