# Techdegree-Project-4

The code provided is a simple inventory management system that allows users to view and add products to a database. The code uses Python and SQLite to manage the database, and SQLAlchemy is used as an ORM to interact with the database.

Instructions on how to work with the game:

Run the program
The program starts with a menu that displays the following options:
Press 'v' to view details of a specific product.
Press 'a' to add a new product to the database.
Press 'b' to create a backup of all the contents of the database.
Press 'e' to exit the program.
Select an option from the menu by typing the corresponding letter and pressing enter.
If you select 'v', you will be prompted to enter the ID of the product you want to view. Enter the ID and press enter.
If the ID entered is not valid, an error message will be displayed, and you will be prompted to enter a valid ID.
If the ID entered is valid, the details of the product will be displayed.
If you select 'a', you will be prompted to enter the name, price, and quantity of the new product.
If you enter an invalid price, an error message will be displayed, and you will be prompted to enter a valid price.
After entering the product details, the product will be added to the database, and a confirmation message will be displayed.
If you select 'b', a backup of all the contents of the database will be created and saved to a CSV file.
If you select 'e', the program will exit.
