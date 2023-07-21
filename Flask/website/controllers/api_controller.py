from ..models import *
from flask_login import current_user
import urllib.request, requests, base64, json


class ApiController:

    def create_api_profile(self, wordpress_username, application_password, application_domain):

        new_api_user = ApiProfile(username=wordpress_username, application_password=application_password,
        application_domain=application_domain, user_id=current_user.id)

        db.session.add(new_api_user)
        db.session.commit()

    def get_user_api(self):
        api_user = ApiProfile.query.filter(ApiProfile.user_id == current_user.id).first()
        return api_user

    def check_api_profile(self):
        exist_api_profile = db.session.query(ApiProfile.id).filter(ApiProfile.user_id==current_user.id).first() is None
        return exist_api_profile

    def api_connection_test(self, application_domain):

        #check if url comes

        request_code = urllib.request.urlopen(application_domain).getcode()
        
        if request_code == 200:
            return True

        else:
            return False

    
    #the registered user has its domain in the database and here it gets called
    def get_api_user_domain(self):

        api_user = self.get_user_api()

        application_domain = api_user.application_domain

        return application_domain


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#TODO get_posts and get_pages in eine function
    #the existing posts in the wordpress application are getting called and displayed on the website of the API
    def get_posts(self, application_domain):

        url_posts = application_domain + "/wp-json/wp/v2/posts"

        posts_json = requests.get(url_posts)

        json_data_list_posts = posts_json.json()

        posts = [(d['id'], d['modified'], d["title"].get("rendered")) for d in json_data_list_posts]

        posts = [list(tup) for tup in posts]
    
        return posts

    
        #the existing pages in the wordpress application are getting called and displayed on the website of the API
    def get_pages(self, application_domain):

        url_pages = application_domain + "/wp-json/wp/v2/pages"

        pages_json = requests.get(url_pages)

        json_data_list_pages = pages_json.json()

        pages = [(d['id'], d['modified'], d["title"].get("rendered")) for d in json_data_list_pages]

        pages = [list(tup) for tup in pages]
    
        return pages

    #this function gets the login data of the user for the API
    def get_api_user(self):

        api_user = self.get_user_api()

        wordpress_username = api_user.username
        application_password = api_user.application_password
        application_domain = api_user.application_domain

        return wordpress_username, application_password, application_domain


    #to connect with wordpress there is an auth needed which contains of the username and the application password
    def auth_connection_api(self, wordpress_username, application_password, application_domain):

        url = application_domain + "/wp-json/wp/v2"

        user = wordpress_username

        #Test Data

        #"pGiW CP0x iH88 kTqi gMrD CHch"
        #http://localhost/wordpress_itc_plugin
        #derAdlige

        creds = user + ":" + application_password

        token = base64.b64encode(creds.encode())

        header = {"Authorization": "Basic " + token.decode("utf-8")}

        return url, header

    
        #this function turns the code into the right form to send it to wordpress 
    #it has to be wrapped up by a script tag that wordpress api gets the code in the right format
    def format_json(meta_tag_data):

        meta_tag_data = json.dumps(meta_tag_data, ensure_ascii=False)

        meta_tag_data = '<script>' + meta_tag_data + "</script>"

        return meta_tag_data