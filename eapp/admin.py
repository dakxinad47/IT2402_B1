from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from eapp.models import Category, Product
from flask_admin import Admin
from eapp import app, db

admin = Admin (app=app, name ="Taicute Mobile Admin")

class ProductView(ModelView):
    column_list = ['id', 'name', 'category', 'price', 'category_id']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    page_size = 10

class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name='Thống Kê Báo Cáo'))
