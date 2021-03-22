import streamlit as st

from utility.consortium_dashboard import consortium_dashboard

def consumer_dashboard():
    pass

def supplier_dashboard():
    pass

def transport_dashboard():
    pass

def merchant_dashboard():
    pass

def main():
    st.title('Food Provenance')
    menu = ['About', 'Consortium', 'Consumer', 'Supplier', 'Transport', 'Merchant']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Consortium':
        consortium_dashboard()
    elif choice == 'Consumer':
        consumer_dashboard()
    elif choice == 'Supplier':
        supplier_dashboard()
    elif choice == 'Transport':
        transport_dashboard()
    elif choice == 'Merchant':
        merchant_dashboard()
    else:
        st.subheader('About')

if __name__ == '__main__':
    main()