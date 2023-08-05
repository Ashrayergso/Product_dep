# Product Catalog Application User Manual

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [How to Use](#how-to-use)
4. [Troubleshooting](#troubleshooting)
5. [Conclusion](#conclusion)

## Overview
The Product Catalog Application is designed to serve the in-house purchasing department by maintaining an accurate, updated list of products. It's precisely made to allow common product purchases rather than catering to retail user flows.

## Installation
To install the Product Catalog Application, follow the steps below:

1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Run the deployment script by typing `python deployment/deploy.py` in your terminal.
4. The script will install all necessary dependencies and set up the environment for you.

## How to Use
The Product Catalog Application is easy to use. Follow the steps below:

1. Run the Streamlit application by typing `streamlit run frontend/streamlit_app.py` in your terminal.
2. Open your web browser and go to `localhost:8501` to view the application.
3. The main page displays a list of products. Each product card contains the product name, description, product number, vendor name, cost, product image, and a link to the product site.
4. You can perform CRUD operations (Create, Read, Update, Delete) on the products.
5. To add a new product, click on the 'Add Product' button and fill in the necessary details.
6. To update a product, click on the 'Update' button on the product card, make the necessary changes, and click 'Save'.
7. To delete a product, click on the 'Delete' button on the product card.
8. You can also export the product list by clicking on the 'Export' button.
9. The search feature allows you to look for product alternatives online. Enter the product name in the search bar and click 'Search'.

## Troubleshooting
If you encounter any issues while using the Product Catalog Application, please refer to the following:

- Make sure you have the correct Python version installed.
- Ensure all dependencies are installed. You can check this in the `deployment/requirements.txt` file.
- If the application doesn't run, make sure the database connection is properly set up in the `backend/database.py` file.

## Conclusion
The Product Catalog Application is a powerful tool for in-house purchasing departments, adding efficiency and convenience. It allows for accurate recording of product details, maintaining an updated product list, and easily comparing market alternatives.