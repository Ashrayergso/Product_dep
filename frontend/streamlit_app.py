```python
import streamlit as st
from backend.controllers import product_controller

def main():
    st.title('Product Catalog Application')

    menu = ["Home", "Search", "Add Product", "Update Product", "Delete Product"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        products = product_controller.read_product()
        for product in products:
            st.text(product['name'])
            st.text(product['description'])
            st.text(product['product_number'])
            st.text(product['vendor_name'])
            st.text(product['cost'])
            st.image(product['image'])
            st.text(product['link'])

    elif choice == "Search":
        st.subheader("Search Product")
        search_term = st.text_input("Enter product name")
        results = product_controller.search_product(search_term)
        for result in results:
            st.text(result['name'])
            st.text(result['description'])
            st.text(result['product_number'])
            st.text(result['vendor_name'])
            st.text(result['cost'])
            st.image(result['image'])
            st.text(result['link'])

    elif choice == "Add Product":
        st.subheader("Add New Product")
        product_data = {}
        product_data['name'] = st.text_input("Enter product name")
        product_data['description'] = st.text_input("Enter product description")
        product_data['product_number'] = st.text_input("Enter product number")
        product_data['vendor_name'] = st.text_input("Enter vendor name")
        product_data['cost'] = st.text_input("Enter product cost")
        product_data['image'] = st.text_input("Enter product image URL")
        product_data['link'] = st.text_input("Enter product link")
        if st.button("Add Product"):
            product_controller.create_product(product_data)

    elif choice == "Update Product":
        st.subheader("Update Product")
        product_number = st.text_input("Enter product number")
        product_data = {}
        product_data['name'] = st.text_input("Enter new product name")
        product_data['description'] = st.text_input("Enter new product description")
        product_data['vendor_name'] = st.text_input("Enter new vendor name")
        product_data['cost'] = st.text_input("Enter new product cost")
        product_data['image'] = st.text_input("Enter new product image URL")
        product_data['link'] = st.text_input("Enter new product link")
        if st.button("Update Product"):
            product_controller.update_product(product_number, product_data)

    elif choice == "Delete Product":
        st.subheader("Delete Product")
        product_number = st.text_input("Enter product number")
        if st.button("Delete Product"):
            product_controller.delete_product(product_number)

if __name__ == "__main__":
    main()
```