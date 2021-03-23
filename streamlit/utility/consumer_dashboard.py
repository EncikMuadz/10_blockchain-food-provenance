import streamlit as st

def consumer_dashboard():
    st.header('Consumer Dashboard')
    menu = ['Home', 'Search']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Search':
        pass

    else:
        st.subheader('Home')