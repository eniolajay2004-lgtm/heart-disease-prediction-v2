import pickle
import streamlit as st

# It is better practice to load the model once using st.cache_resource
@st.cache_resource
def load_model():
    with open('rfmodel.pkl', 'rb') as pickle_in:
        clf = pickle.load(pickle_in)
    return clf

clf = load_model()

@st.cache_data
def make_prediction(Age, EstSalary, Gender):
  if Gender == "Male":
    GenderM = 1
    GenderF = 0
  elif Gender == "Female":
    GenderM = 0
    GenderF = 1

  prediction = clf.predict([[Age, EstSalary, GenderF, GenderM]])[0]

  if prediction == 0:
    value = "not to purchase"
  else:
    value = "to purchase"
  return value

def main():
    #front end elements
    html_temp = """
    <div style ="background-color:green;padding:13px">
    <h1 style ="color:white;text-align:center;">SUNPAUL' Insurance Prediction</h1>
    </div>
    """

    #front end
    #st.markdown ('![](logo2.png)')
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    Age = st.number_input('Enter the Age')
    EstSalary = st.number_input('Enter Estimated Salary')
    Gender = st.selectbox('Gender',("Male","Female"))
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Make Prediction"):
        result = make_prediction(Age, EstSalary, Gender)
        st.success(f'This customer is likely {result}')
        print("Just test")

if __name__=='__main__':
  main()
