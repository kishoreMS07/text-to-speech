import streamlit as st
from gtts import gTTS
import tempfile
import os


def text_to_speech(text):
    tts = gTTS(text=text, lang="en", tld="co.in")
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_name = temp_file.name
    tts.save(temp_file_name)
    return temp_file_name


def main():
    st.title("Text-to-Speech Generator")
    text = st.text_area(
        "Enter text to convert to speech",
        placeholder="Enter your text here to speak...",
    )
    if st.button("Convert to Speech"):
        if text:
            audio_file = text_to_speech(text)
            st.audio(audio_file, format="audio/mp3")
            os.remove(audio_file)
        else:
            st.warning("Please enter some text to convert to speech.")


if __name__ == "__main__":
    main()
