from sqlalchemy import (
    MetaData, Table, Column, Integer, Float, DateTime, ForeignKey
)


metadata = MetaData()

orders = Table(
    'orders', metadata,
    Column('number', Integer, primary_key=True),
    Column('order_date', DateTime),
)

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True),
    Column('order', ForeignKey('orders.number')),
    Column('price', Float),
    Column('quantity', Integer),
)
