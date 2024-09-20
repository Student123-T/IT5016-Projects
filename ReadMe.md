**                                                  Grocery Store [Scan Items And Register Users]                                     **
-->Overview:
The Grocery Store Application is a simple console-based program that allows users to 
-register
-add items to their cart
-complete a checkout process
It demonstrates object-oriented programming principles using classes to represent items, users, and the grocery store itself.

-->Features:
Item Management:
-The store allows the addition of items with a name and price.

User Registration: 
-Users can register with a unique username and email.

Shopping Cart: 
-Each user has a cart where they can add items.

Add to Cart: 
-Users can add available items to their cart.

View Cart: 
-Users can view all items in their cart along with the total price.

Checkout: 
-Users can complete their purchase, which clears their cart.

Interactive Item Addition: 
-Items can be added to the store interactively via user input.

--Software Design Principles:
>Single Responsibility Principle
--Each class in the application has a single responsibility:
-Item: Responsible for holding item details (name and price).
-User: Manages user information and cart operations.
-GroceryStore: Handles item management and user registration.

>DRY Principle (Don't Repeat Yourself)
--By creating methods like add_to_cart, view_cart, and checkout, the code avoids repetition. Each functionality is implemented once and reused as needed.

>Composition over Inheritance
--The design uses composition (combining objects) rather than inheritance. For instance, the User class contains a list of Item objects instead of extending an Item class. This makes it flexible and easier to manage relationships.

>KISS [Keep It Simple, Stupid]
-Emphasizes simplicity in design. 

--Here’s how it applies to your Grocery Store application:
-Simple Class Structure:
Three clear classes (Item, User, GroceryStore) each have a specific purpose, making the code easy to understand.
-Straightforward Methods:
Methods like add_to_cart perform single, clear actions without unnecessary complexity.
-User-Friendly Input:
Prompts for user input are simple and direct, guiding users easily through interactions.
-Basic Data Structures:
Uses simple lists and dictionaries for managing items and users, avoiding complex data structures.

--User Interaction Flow:
-Adding Items: Users can interactively add items to the store.
-User Registration: Users provide their username and email to register.
-Adding Items to Cart: Registered users can add items by name to their cart.
-Viewing Cart: Users can view their cart contents.
-Checkout: Users can complete their purchase, and their cart will be emptied.

|----- Grocery_Store.py # Main Code file containing
|----- ReadMe.md        # Project Documentation

//How to Run//
1.Ensure you have Python installed on your machine.

2.Copy the code into a Python file (e.g., grocery_store.py).

3.Run the file using the command:
python grocery_store.py

-Follow the steps to interact with the grocery store system!
