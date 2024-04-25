import streamlit as st
import os
import imageio
import tensorflow as tf

from utils import load_data, num_to_char
from modelutil import load_model

# Set layout


with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title("About")
    st.info("In this Section the Lip reaading is done pre defined DataSet")

st.title('LipReding 🗣️')
# Retrieve the list of videos
videos = os.listdir(os.path.join('..', 'data', 's1'))
selected_video = st.selectbox('Pick a video', videos)

# Generate 2 columns
col1, col2 = st.columns(2)

if videos:
    with col1:
        st.info('Chosen video:')
        file_path = os.path.join('..', 'data', 's1', selected_video)
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

        # Rendering soumya main 
        
    with col2:
        hehe = st.info('Input for model:')
        video, annotations = load_data(tf.convert_to_tensor(file_path))
        imageio.mimsave('animation.gif', video, fps=10)
        st.image('animation.gif', width=500)

        st.info('Tokenized prediction:')
        model = load_model()
        yhat = model.predict(tf.expand_dims(video, axis=0))
        # Greedy algorithm takes most probable prediction
        decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
        st.text(decoder)

        # Decode prediction
        st.info('Decoded prediction into text:')
        converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('UTF-8')
        st.text(converted_prediction)