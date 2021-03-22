import streamlit as st

def add_participants():
    pass

def remove_participant():
    pass

def view_all_ledger():
    pass

def consortium_dashboard():
    st.header('Consortium Dashboard')
    menu = ['Home', 'Manage Network', 'Ledgers', 'Search']
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == 'Home':
        st.subheader('Home')
    
    elif choice == 'Manage Network':
        add_participants()
        remove_participant()
        
    elif choice == 'Ledgers':
        view_all_ledger()

    elif choice == 'Search':
        pass
    
    else:    
        st.subheader('Home')    