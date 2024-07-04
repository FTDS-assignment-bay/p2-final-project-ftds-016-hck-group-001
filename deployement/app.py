import streamlit as st
import eda, predict

# Define the Home Page
def show_home():
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>Complaint Ease</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write('')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image('ComplaintEase.png')  
    st.write('')
    st.write('''This application is specifically designed to facilitate both exploratory data analysis and predictive modeling regarding airline reviews. It provides users with advanced analytical tools that help in understanding trends and patterns within the data. To begin, please use the navigation menu on the left side of the screen to select the particular module that you intend to explore. Whether you're looking to uncover insights or forecast future trends, this tool equips you with the necessary resources to effectively analyze the feedback from airline passengers.''')
    st.markdown('---')
    
# Add side bar for navigation
PAGES = {
    "Home" : show_home,
    "Exploratory Data Analysis": eda,
    "Make Predictions": predict
 
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''bla bla bla ''')

# Features
st.sidebar.write('''### Key Features:
bla blba bla ''')

# Target Audience
st.sidebar.write('''### Who can benefit?
bla bla bla .''')

if selection == 'Home':
    show_home()
elif selection == 'Exploratory Data Analysis':
    eda.app()
elif selection == 'Make Predictions':
    predict.app()
