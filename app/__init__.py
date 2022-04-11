from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
DB_NAME = "products.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:marcospaulo14@localhost/products'

    db = SQLAlchemy(app)
    db.init_app(app)
    #db.create_all(app=app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(views, url_prefix='/registry')
    app.register_blueprint(views, url_prefix='/remove')
    app.register_blueprint(views, url_prefix='/confirma')


    return app
    #metodo que inicializa a aplicação

