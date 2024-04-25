import streamlit as st
import subprocess
with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title("About")
    st.info("In this Section the Lip reaading is done REALTIME")
def run_prediction():
    result = subprocess.run(['python', 'predict_live.py'])
    return result.stdout

def main():
    st.title("Live Prediction")

    st.write("Click the button below to run the live prediction.")

    if st.button("Run Prediction"):
        prediction_result = run_prediction()
        st.write("Prediction Result:")
        st.code(prediction_result)
st.write("Click ESC button to end the task")
if __name__ == "__main__":
    main()
