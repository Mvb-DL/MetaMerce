from ..models import ExtractedProduct, db
from flask_login import current_user

class ProductController:

    def delete_user_product(self, product_id):
        db.session.query(ExtractedProduct).filter(ExtractedProduct.id == product_id).delete()
        db.session.commit()

    #counts the number products of the user
    def count_products(self):
        number_products = ExtractedProduct.query.count()
        return number_products

    def get_products_user(self):
        user_products = ExtractedProduct.query.filter(ExtractedProduct.user_id == current_user.id).all()
        return user_products

    def get_exact_product(self, value):
        extracted_product = ExtractedProduct.query.filter(ExtractedProduct.id == value).first()
        return extracted_product

    def create_product(self, title, description, price, brand, low_price, high_price, currency, country, category, belonging_company, filename, imagetext):

        new_product = ExtractedProduct(title=title, description=description, price=price,
          brand=brand, low_price=low_price, high_price=high_price,
          currency=currency, country=country, category=category, filename=filename,                   
          belonging_company=belonging_company, user_id=current_user.id, imagetext=imagetext)

        db.session.add(new_product)
        db.session.commit()
        
        return new_product
