DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS product_categories;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE product_categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    telephone_number INT,
    address VARCHAR(255)
);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    quantity INT,
    purchase_price INT,
    selling_price INT,
    date_and_time VARCHAR(255),
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    product_category_id INT REFERENCES product_categories(id) ON DELETE CASCADE
);