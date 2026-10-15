from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Product: {self.name}  Precio: {self.price}  Stock: {self.stock}"

def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada ")

def insert_products():
    with app.app_context():
        producto1 = Product(name="Coca cola", price=15.00, stock=50)
        producto2 = Product(name="fanta", price=15.00, stock=45)
        producto3 = Product(name="cocaquina", price=10.00 , stock= 80)
        producto4 = Product(name="salvieti", price=12.00 , stock= 9)
        producto5 = Product(name="acuarius", price=25.00 , stock= 18)

        db.session.add(producto1)
        db.session.add(producto2)
        db.session.add(producto3)
        db.session.add(producto4)
        db.session.add(producto5)
        db.session.commit()
        print("Productos insertados correctamente")


def query_products():
    with app.app_context():
        print("--------------------------------------")
        print("---Listado completo de productos ---")
        products = Product.query.all()
        for item in products:
            print(item)   
        print(" Productos con precio mayor a 10")
        caros = Product.query.filter(Product.price > 10).all()
        for item in caros:
            print(item)

        print("--- Registro único ---")
        product = Product.query.filter_by(id=1).first()
        if product:
            print(product)

def update_product():
    with app.app_context():
        print("--------------------------------------")
        print("--- Actualizando un producto ---")
        product = Product.query.filter_by(id=2).first()
        if product:
            product.price = 12.00
            product.stock = 20
            db.session.commit()
            print("Producto actualizado con éxito:", product)
        else:
            print("Producto no encontrado.")

def delete_product():
    with app.app_context():
        print("--------------------------------------")
        print("--- Eliminando un producto ---")
        product = Product.query.filter_by(id=3).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            print("El producto ha sido eliminado.")
        else:
            print("Producto no encontrado.")

if __name__ == "__main__":

    init_db()          
    insert_products()  
    query_products()   
    update_product()   
    delete_product()  