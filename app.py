from models import (Base, session, Product, engine)
import datetime
import csv
import time


# def add_csv():
#     with open('inventory.csv') as csvfile:
#         data = csv.reader(csvfile)
#         for row in data:
#             product_in_db = session.query(Product).filter(Product.title ==row[0]).one_or_none()
#             if product_in_db == None:
#                 title = row[0]
#                 author = row[1]
#                 date = (clean_date(row[2]))
#                 price = clean_price(row[3])
#                 new_book = Book( title = title, author = author, 
#                             published_date =  date, price = price)
#                 session.add(new_book)
#         session.commit()
     

if __name__ == "__main__":
    Base.metadata.create_all(engine)

