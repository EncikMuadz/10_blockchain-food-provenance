import streamlit as st

def merchant_dashboard():
    st.header('Merchant Dashboard')
    menu = ['Home', 'Manage Inventory', 'Search']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Manage Inventory':
        st.subheader('Inventory Management')

    elif choice == 'Search':
        pass

    else:
        st.subheader('Home')