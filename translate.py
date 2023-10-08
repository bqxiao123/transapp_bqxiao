import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
from google_trans_new import google_translator
from deep_translator import GoogleTranslator
import streamlit_authenticator as stauth
import os



# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
# st.write(name,authentication_status, username)
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    # st.write(f'Welcome *{st.session_state["username"]}*')
    # st.title('Some content')
    if username not in os.listdir('users'):
        os.mkdir('users/'+username)

    abs_pth = os.path.abspath('users/'+username)

    if "new_word.txt" in os.listdir('users/'+username):
        with open(f"{abs_pth}/new_word.txt", "r") as f:
            word = f.readlines()
    else:
        word=[]


    # st.markdown(word)

    col1, col2 = st.columns(2)

    translator = GoogleTranslator(source='auto', target='zh-CN')
    st.sidebar.markdown("## Translate with GOOGLE API")
    text = st.sidebar.text_area("translats", "translate")
    # # 将英文文本翻译成中文
    translated_text = translator.translate(text)
    # col1.write("Original Image :camera:")
    col1.markdown(text)
    col2.markdown(translated_text)
    new_wd = st.text_input("new word:", "")
    if new_wd not in [x.strip() for x in word]:
        with open(f"{abs_pth}\\new_word.txt", "a") as f:
            if len(word) < 1:
                f.writelines(new_wd)
            else:
                f.writelines("\n" + new_wd)

    st.sidebar.markdown("## Select Data Time and Detector")

    upload_img = st.sidebar.file_uploader("Upload Image")

    if upload_img:
        img = Image.open(upload_img)
        grey_img = img.convert("L")
        st.image(grey_img)
        text = pytesseract.image_to_string(img)
        # st.markdown(text)
        # 创建翻译器对象
        translator = Translator()

        #
        # # 将英文文本翻译成中文
        translated_text = translator.translate(text, src='en', dest='zh-CN')
        # print(text)
        # st.markdown(translated_text.text)

    # 打印翻译结果
    # print("英文单词:", english_text)
    # print("中文翻译:", translated_text.text)

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

##test


