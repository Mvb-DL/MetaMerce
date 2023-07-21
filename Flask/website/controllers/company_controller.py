from ..models import *
from flask_login import current_user

class CompanyController:

    def create_company(self, company_name, company_type, company_website_name, company_url, company_selling_category):
        new_company = Company(company_name=company_name, company_type=company_type,
        company_website_name=company_website_name, company_url=company_url,
        company_selling_category=company_selling_category, user_id=current_user.id)
        db.session.add(new_company)
        db.session.commit()

    def delete_user_company(self, company_id):
        db.session.query(Company).filter(Company.id == company_id).delete()
        db.session.query(ExtractedProduct).filter(ExtractedProduct.belonging_company == company_id).delete()
        db.session.commit()

    def get_user_company(self):
        user_company = Company.query.filter(Company.user_id == current_user.id).all()
        return user_company

    def check_user_company(self):
        exist_company = db.session.query(Company.id).filter(Company.user_id == current_user.id).first() is None
        return exist_company

    def get_current_user_company(self):
        current_company = db.session.query(Company).filter(Company.user_id==current_user.id).first_or_404()
        return current_company

    def get_belonging_company(self):
         user_company = self.get_current_user_company()
         company_id = user_company.id
         return company_id
    