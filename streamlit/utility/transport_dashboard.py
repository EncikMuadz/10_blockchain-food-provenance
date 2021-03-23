import streamlit as st

def transport_dashboard():
    st.header('Transport Dashboard')
    menu = ['Home', 'Manage inventory', 'Lokasi']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Manage Inventory':
        st.subheader('Inventory Management')

    elif choice == 'Lokasi':
        pass

    else:
        st.subheader('Home')