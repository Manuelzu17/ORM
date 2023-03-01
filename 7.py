from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Tabla de productos
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000))
    price = Column(Integer, nullable=False)

# Tabla de clientes
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(1000))

    # Relación uno a muchos con la tabla de pedidos
    orders = relationship("Order", back_populates="customer")

# Tabla intermedia para la relación muchos a muchos entre pedidos y productos
order_product = Table('order_product', Base.metadata,
    Column('order_id', ForeignKey('orders.id'), primary_key=True),
    Column('product_id', ForeignKey('products.id'), primary_key=True)
)

# Tabla de pedidos
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    shipping_info = Column(String(1000))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Relación muchos a uno con la tabla de clientes
    customer = relationship("Customer", back_populates="orders")

    # Relación muchos a muchos con la tabla de productos
    products = relationship("Product", secondary=order_product, back_populates="orders")
