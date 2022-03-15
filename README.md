# full_stack_project_shop_inventory_day_20

This is a program that helps companies manage their inventory. As a young person I spend hours and hours counting the stock in my grandfathers
warehouse. This program is dedicated to the younger version of me and the days lost mindlesly counting shelf after shelf of inventory.
The program allows the user to add Categories,Manufacturers,Suppliers and Products which they can edit and delete.
It can help you keep track of stock, orders, debt and many other important pieces of information that are needed for your inventory.

To run the project you will need Flask, Psycopg2, Python, Html, Postgresql

The recommended browser is Google Chrome.

#terminal

run flask

dropdb shop_inventory
createdb shop_inventory
psql -d shop_inventory -f db/shop_inventory.sql

python3 console.py

Open in Google Chrome using LocalHost:5000

PROJECT BRIEF

### Shop Inventory

Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

#### MVP

* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
  * This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

#### Inspired by

eBay, Amazon (back end only), Magento

#### Possible Extensions

* Calculate the markup on items in the store, and display it in the inventory
* Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
* Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
* Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

<img width="1280" alt="Screenshot 2022-03-15 at 09 46 10" src="https://user-images.githubusercontent.com/83923406/158351512-b56e312a-1471-4f79-ad4a-d90afb127f42.png">
<img width="1279" alt="Screenshot 2022-03-15 at 09 46 31" src="https://user-images.githubusercontent.com/83923406/158351561-e1da9169-0fba-4836-bcb1-1a10d971c297.png">
<img width="1279" alt="Screenshot 2022-03-15 at 09 46 44" src="https://user-images.githubusercontent.com/83923406/158351610-202b1501-dfa1-4c03-bf78-7631bf08db8d.png">
<img width="1279" alt="Screenshot 2022-03-15 at 09 47 08" src="https://user-images.githubusercontent.com/83923406/158351627-bf018133-c587-4caa-88ad-8ce4919a7031.png">
