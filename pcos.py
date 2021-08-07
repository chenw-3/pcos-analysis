import streamlit as st
import pandas as pd
import pickle
import string
from sklearn.ensemble import RandomForestRegressor


#load model
model=pickle.load(open('pcos_model.pkl', 'rb'))

#@st.cache #this func will be cached
def main():
    #Title
    st.title('Welcome to your PCOS Predictor!')

    #header
    st.header('This tool is meant to predict your likelihood of having Polycystic Ovarian Syndrome (PCOS)')

    #Subheader
    st.markdown('PCOS is a condition that affects 1 in 10 women. It often goes undiagnosed with symptoms like irregular periods, excessive hair growth, weight gain, anxiety and depression. This tool is meant to assess your symptoms and tell you if PCOS could be the cause of them.')

    #sidebar
    #st.sidebar.slider('Slider')

    #ballons
    #st.balloons()

    col1, col2 = st.beta_columns(2)

    with col1:
        st.header('Fill out the form:')

        #instructions
        st.subheader('Select Yes - 1 or No - 0 for each symptom:')

        #create form
        form = st.form('pcos_form')


    weight_gain = form.number_input(
        'Weight gain', min_value = 0, max_value = 1)

    #irregular periods
    periods = form.number_input(label='Irregular Periods', min_value = 0, max_value = 1)

    #excessive hair growth
    hair_growth = form.number_input(label='Excessive Hair Growth',  min_value = 0, max_value = 1)

    #darkened skin
    darkskin = form.number_input(label='Skin darkening',  min_value = 0, max_value = 1)

    #regular fast food consumption
    fast_food = form.number_input(label='Do you consume Fast Food regularly?',  min_value = 0, max_value = 1)
    
    #form.form_submit_button('Submit')
    
    inputs = [[weight_gain, hair_growth, darkskin, fast_food]]

    if form.form_submit_button('Submit Answers'):
        result = model.predict(inputs)
        if result == 0:
            st.write("Congrats! Chances are you don't have PCOS!")

        else:
            st.write('It is likely you suffer from PCOS. Please consult with your physician.')


        #form.success('Your PCOS prediction is {}'.form(updated_results))
    
    #submit button
    #form.form_submit_button("Submit")


if __name__ == '__main__':
    main()
