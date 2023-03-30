import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

panic_model = pickle.load(open('panicpred.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Panic Prediction System',
                          
                          ['Panic Prediction',
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Panic Prediction'):
    
    # page title
    st.title('Panic Prediction using ML')
    
    
    # getting the input data from the user
    col1 = st.columns(1)
    
    with col1:
        hr = st.text_input('hr value')
        HR = hr

    # code for Prediction
    panic_diagnosis = ''
    hr_data = [hr,hr-1,hr+2,hr-2,hr+4]
    rr_data = [60000/hr for hr in hr_data]
    MEAN_RR = np.mean(rr_data)
    MEDIAN_RR = np.median(rr_data)
    

    # creating a button for Prediction
    
    if st.button('Panic Test Result'):
        panic_prediction = panic_model.predict([[HR,MEAN_RR,MEDIAN_RR]])
        
        if (panic_prediction[0] == 1):
          panic_diagnosis = 'The person is panic'
        else:
          panic_diagnosis = 'The person is not panic'
        
    st.success(panic_diagnosis)



