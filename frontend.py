import streamlit as st
import requests

st.title("Mushroom Classifier 🍄")

st.write("Enter the features of the mushroom to predict if it's edible or poisonous.")

odor= st.selectbox("Odor", options=['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm'])
gillsize= st.selectbox("Gill Size", options=['b', 'n'])
stalksurfacebelowring= st.selectbox("Stalk Surface Below Ring", options=['s', 'f', 'y', 'k'])
stalksurfaceabovering= st.selectbox("Stalk Surface Above Ring", options=['s', 'f', 'y', 'k'])

if st.button("Predict"):
    params = {
        "odor": odor,
        "gillsize": gillsize,
        "stalksurfacebelowring": stalksurfacebelowring,
        "stalksurfaceabovering": stalksurfaceabovering
    }

    base = "https://mushroom-detector-459825881583.europe-west1.run.app"
    URL = f"{base}/predict"

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"The mushroom is predicted to be: {prediction}")
    else:
        st.error("Error in prediction. Please try again.")

#change
# # dajklfhgdasfgadsfdisaufgas
