from models import (Base, session, Product, engine)
import datetime
import csv
import time

def menu():
    choice =input(''' 
    \n***** Main Menu *****
    \rPlease make a selection
    \rPress 'v' View details
    \rPress 'a' to add item
    \rpress 'b' to make a back up of all contets
    \rPress 'e' to exit
    \r
    \rMake your selection: ''')

    if choice in ['v', 'a', 'b', 'e' ]:
        return choice

def clean_date(date_str):
    try:
        date_object = datetime.datetime.strptime(date_str, "%m/%d/%Y")
        format_date =date_object.strftime("%Y-%m-%d")
        return_date = datetime.datetime.strptime(format_date, '%Y-%m-%d').date()

    except ValueError:
        input( ''' 
            \n******** DATE ERROR *********
            \rThe Date format should inlcude a valid Month Day, Year from the past
            \rExample: January 13, 2003
            \rPress ENTER to try again
            \r********************************* 
            \r''')
        return

    else:
        return return_date



def clean_price(price_str):
    cleaned_price = float(price_str.strip("$"))
    cleaned_price = float(cleaned_price)
    cleaned_price = int(cleaned_price * 100)
    return cleaned_price



def clean_id(id_str, options):
    try:
        product_id = int(id_str)
    except:
        input( f''' 
            \n******** Id ERROR *********
            \rId must be a number.
            \rPress ENTER to try again
            \r***************************''')
        return
    else:
        if product_id in options:
            return product_id
        else:
            input( f''' 
            \n******** Id ERROR *********
            \rOptions are: {options}.
            \rPress ENTER to try again
            \r***************************''')

def clean_data(data):
    new_data =[]
    for row in data:
        clean_rows = {}
        clean_rows['product_name'] = row['product_name']
        prices = row['product_price']
        prices = clean_price(prices)
        clean_rows['product_price'] = prices
        quants = row['product_quantity']
        quants = int(quants)
        clean_rows['product_quantity'] = quants
        dates = row['date_updated']
        dates = clean_date(dates)
        clean_rows['date_updated'] = dates
        new_data.append(clean_rows)
    return new_data


    
def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.DictReader(csvfile)
        new_data = clean_data(data)
        for row in new_data:
            product_with_same_name = session.query(Product).filter(Product.product_name == row['product_name']).first()
            if not product_with_same_name:
                new_product = (Product(product_name = row['product_name'], product_price = row['product_price'],
                                    product_quantity = row['product_quantity'], date_updated = row['date_updated']))
                session.add(new_product)
        session.commit()


def app():
    add_csv()
    app_running = True
    while app_running:
         choice = menu()
         if choice == 'v':
            id_options = []
            for item in session.query(Product):
                id_options.append(item.product_id)
            id_error = True
            while id_error:
                pick_id = input(f'''
                \nId options = {id_options}
                \rMake your selection: ''')
                pick_id = clean_id(pick_id, id_options)
                if type(pick_id) == int:
                    id_error = False
            the_product = session.query(Product).filter(Product.product_id == pick_id).first()
            print(f'''
                  \nProduct name: {the_product.product_name}
                  \rProduct Price: ${(the_product.product_price) / 100}
                  \rStock:  {the_product.product_quantity}
                  \rStock updated on: {(the_product.date_updated)}  
                  \r''')
            input('Press ENTER to continue')

         elif choice == 'a':
            pass

         elif choice ==  'b':
            pass

         else:
            print("Inventory Closing: Goodbye!")
            app_running = False
        
     
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    app()

   
    
    

    

