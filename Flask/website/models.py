from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash


#upload-model
class Upload(db.Model):

    __tablename__ = 'upload'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, data, date):
        self.data = data
        self.date = date

#user-model
class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    user_name = db.Column(db.String(128), nullable=False, unique=True)
    create_user_date = db.Column(db.Date(), default=func.now())

    uploads = db.relationship('Upload', backref="user")
    extracted_product = db.relationship('ExtractedProduct', backref="user")
    company = db.relationship('Company', backref="user")
    api_profile = db.relationship('ApiProfile', backref="user")

    def __init__(self, email, password, first_name, last_name, user_name):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)


#company of the User
class Company(db.Model):

    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(128), nullable=False)
    company_type = db.Column(db.String(128))
    company_website_name = db.Column(db.String(128))
    company_url = db.Column(db.String(128), nullable=False)
    company_selling_category = db.Column(db.String(128))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, company_name, company_type, company_website_name, company_url, company_selling_category, user_id):
        self.company_name = company_name
        self.company_type = company_type
        self.company_website_name = company_website_name
        self.company_url = company_url
        self.company_selling_category = company_selling_category
        self.user_id = user_id
    

#extracted product
class ExtractedProduct(db.Model):

    __tablename__ = 'extracted_product'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(512), nullable=True, default=None)
    price = db.Column(db.String(24), nullable=True, default=None)
    low_price = db.Column(db.String(24), nullable=True, default=None)
    high_price = db.Column(db.String(24), nullable=True, default=None)
    title = db.Column(db.String(256), nullable=True, default=None)
    brand = db.Column(db.String(256), nullable=True, default=None)
    currency = db.Column(db.String(24), nullable=True, default=None)
    category = db.Column(db.String(128), nullable=True, default=None)
    country = db.Column(db.String(128), nullable=True, default=None)
    filename = db.Column(db.String(128), nullable=True, default=None)
    imagetext = db.Column(db.String(512), nullable=True, default=None)
    meta_tag_code_json_ld = db.Column(db.String(1024), nullable=True, default=None)
    meta_tag_code_rdf = db.Column(db.String(1024), nullable=True, default=None)
    meta_tag_code_microdata = db.Column(db.String(1024), nullable=True, default=None)

    belonging_company = db.Column(db.Integer, db.ForeignKey('company.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#new subsriper-model
class SubscriperUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)


#new API Profile
class ApiProfile(db.Model):

    __tablename__ = 'api_profile'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    application_password = db.Column(db.String(128), nullable=False)
    application_domain = db.Column(db.String(128), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))