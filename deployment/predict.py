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
nltk.dowload('wordnet')
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
    
    return predictions_list

def response(x):
    if x in ([0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 1, 1]):
        return 'Requires Immediate Attention'
    else:
        return 'Follow The Standard Time Protocol'

def process_csv(file, model):
    # Read CSV
    data = pd.read_csv(file)
    data['complaint_id'] = data['complaint_id'].astype(str)
    
    # Preprocess text and predict sentiment
    data['narrative'] = data['issue'] + ' ' + data['sub_issue'] + ' ' + data['consumer_complaint_narrative']
    
    sentences = data['narrative'].apply(text_preprocessing)
    pred = predict_sentiment(sentences, model)
    
    # Apply the response function to each element in pred
    responses = [response(x) for x in pred]
    data['response'] = responses

    # Select required columns and format predictions
    output = data[['complaint_id', 'product', 'response']]
    return output

def app():
    st.title('Predict Complaint Level')

    option = st.selectbox(
        'Choose input method',
        ('Upload CSV', 'Manual Input')
    )

    if option == 'Upload CSV':
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_file is not None:
            with st.spinner('Processing...'):
                output = process_csv(uploaded_file, model)
                st.dataframe(output)
    elif option == 'Manual Input':
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
                
                responses = response(predictions)
    
                # Display the prediction result
                st.success(f'Prediction: {responses}')
        else:
            st.warning("Please fill the complaint.")

if __name__ == '__main__':
    app()