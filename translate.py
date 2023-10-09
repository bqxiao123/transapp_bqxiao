import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
from google_trans_new import google_translator
from deep_translator import GoogleTranslator
# import streamlit_authenticator as stauth
import os

wd_file = "bqxiao"


if wd_file not in os.listdir('users'):
    os.mkdir('users/'+wd_file)
abs_pth = os.path.abspath('users/'+wd_file)

if "new_word.txt" in os.listdir('users/'+wd_file):
    with open(f"{abs_pth}/new_word.txt", "r") as f:
        word = f.readlines()
else:
    word = []

word = [x.replace('\n', '') for x in word if x != '\n']

col1, col2 = st.columns(2)

translator = GoogleTranslator(source='auto', target='zh-CN')
st.sidebar.markdown("## Translate with GOOGLE API")
text = st.sidebar.text_area("translats", "")
# # 将英文文本翻译成中文
translated_text = translator.translate(text)
# col1.write("Original Image :camera:")
col1.markdown(text)
col2.markdown(translated_text)
new_wd = st.text_input("Input your new word here:", "").strip()

if new_wd not in [x.strip() for x in word]:
    print(word, new_wd)
    word = word + [new_wd.strip()]
    word = '\n'.join(word)
    with open(f"{abs_pth}/new_word.txt", "w") as f:
        f.write(word)

#
# print('xxx', type(word), '........')

with open(f"{abs_pth}/new_word.txt", "r") as f:
    word = f.read()
st.download_button('Download your new words', word)


##test


