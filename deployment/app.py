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
    st.write('''After reviewing the customer satisfaction survey result, we've found that 65% of our customers are satisfied with our products. 
             As an initiative to increase our customer's satisfaction, we'll utilize our data department to give us insights on complaints data and 
             deep learning to help us categorized data, which will help us take actions that are suited to each category.''')
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
st.sidebar.write('''This application is specifically designed to categorize and predict customer complaints to help us decide the right action for each category.''')

# Target Audience
st.sidebar.write('''### Who can benefit?
- Head of Customer Service.
- Customer Service Department.''')

if selection == 'Home':
    show_home()
elif selection == 'Exploratory Data Analysis':
    eda.app()
elif selection == 'Make Predictions':
    predict.app()
