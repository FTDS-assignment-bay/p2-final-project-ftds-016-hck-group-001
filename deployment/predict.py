import streamlit as st
import pandas as pd
import tensorflow as tf 
from tensorflow.keras.models import load_model

# for text preprocess
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

# load model
model = load_model('./model/model.keras')

# Define Stopwords
stop_words = set(stopwords.words('english'))

# Define Stemming
lemmatizer = WordNetLemmatizer()

@st.cache_data
# Create A Function for Text Preprocessing
def text_preprocessing(text):
  # Case folding
  text = text.lower()

  # Mention removal
  text = re.sub("@[A-Za-z0-9_]+", " ", text)

  # Hashtags removal
  text = re.sub("#[A-Za-z0-9_]+", " ", text)

  # Newline removal (\n)
  text = re.sub(r"\\n", " ",text)

  # Whitespace removal
  text = text.strip()

  # URL removal
  text = re.sub(r"http\S+", " ", text)
  text = re.sub(r"www.\S+", " ", text)

  # Non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
  text = re.sub("[^A-Za-z\s']", " ", text)
  text = re.sub("'", "", text)

  # Tokenization
  tokens = word_tokenize(text)

  # Stopwords removal
  tokens = [word for word in tokens if word not in stop_words]

  # Stemming
  tokens = [lemmatizer.lemmatize(word) for word in tokens]

  # Combining Tokens
  text = " ".join(tokens)

  return text

def predict_sentiment(review_text, model):
    # Perform prediction
    predictions = model.predict([review_text])
    predictions[:,0] = tf.where(predictions[:,0] > 0.1, 1, 0)  # Thresholding light complaints at 0.1
    predictions[:,1] = tf.where(predictions[:,1] > 0.1, 1, 0)  # Thresholding harsh complaints at 0.1
    predictions[:,2] = tf.where(predictions[:,2] > 0.75, 1, 0) 
    
    # Convert tensor to a list of 1s and 0s
    predictions_list = predictions.tolist()
    
    # Replace 1 with 'Recommending' and 0 with 'Not Recommending'
    # predictions_recommended = ['The author recommending this product' if x == 1 else 'The author not recommending this product' for x in predictions_list]
    
    return predictions_list

def app():
    st.title('Predict Complaint Level')
    
    data = pd.read_csv('data/consumer_complaints_cleaned.csv')

    issue = st.selectbox(
        label='Choose the issue',
        options=data['issue'].unique()
    )
    
    sub_issue = st.selectbox(
        label='Choose the sub issue',
        options=data[data['issue']==issue]['sub_issue'].unique()
    )

    complaint = st.text_area(
        label="Write Your Complaint"
    )

    narative = issue + ' ' + sub_issue + ' ' + complaint
    
    if st.button("Predict"):
        if complaint:
            # Display a loading message while predicting
            with st.spinner('Predicting...'):
                # Perform prediction
                sentence = text_preprocessing(narative)
                
                predictions = predict_sentiment(sentence, model)
    
                # Display the prediction result
                st.success(f'Prediction: {predictions[0]}')
        else:
            st.warning("Please enter a review.")

if __name__ == '__main__':
    app()