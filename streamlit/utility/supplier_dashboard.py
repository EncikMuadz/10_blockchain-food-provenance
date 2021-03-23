import streamlit as st

def supplier_dashboard():
    st.header('Supplier Dashboard')
    menu = ['Home', 'Manage inventory']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Manage Inventory':
        st.subheader('Inventory Management')

    else:
        st.subheader('Home')