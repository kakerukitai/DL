import streamlit as st
import youtube_dl

st.title('youtube ダウンロード')


url = st.text_input('URLを入力してください')

if st.button('開始'):

    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

    buttonurl = url

    with ydl:
        result = ydl.extract_info(
            buttonurl,
            download=True
        )
            


