from eapp.models import Category, Product, User
from eapp import app
import hashlib


def load_categories():
    return Category.query.order_by('id').all()

def load_products(kw = None, cate_id=None, page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id == int(cate_id))

    page_size = app.config["PAGE_SIZE"]
    start = (page-1)*page_size
    #SELECT * ... FROM ... LIMIT 8 OFFSET 3

    return query.order_by('id').slice(start, start + page_size).all()

def product_count():
    return Product.query.count()

def authenticate(username, password):

    return User.query.filter(User.username == username.strip(),
                            User.password == password).first()

def get_user_id(user_id):
    return User.query.get(user_id)