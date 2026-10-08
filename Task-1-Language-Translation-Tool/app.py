import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException


# Page configuration
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="",
    layout="centered"
)

# Title
st.title(" AI Language Translator")
st.write("Translate text into multiple languages with automatic language detection.")

# Supported languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Spanish": "es"
}


def detect_language(text):
    """Detect the language of the input text."""
    try:
        language_code = detect(text)
        return language_code
    except LangDetectException:
        return None


def translate_text(text, target_language):
    """Translate text into the selected language."""
    try:
        translator = GoogleTranslator(
            source="auto",
            target=target_language
        )
        return translator.translate(text)
    except Exception as e:
        return f"Translation error: {e}"


# Text input
text = st.text_area(
    "Enter your text:",
    placeholder="Type or paste your text here...",
    height=150
)

# Detect language
if text.strip():
    detected_code = detect_language(text)

    language_names = {
        "en": "English",
        "hi": "Hindi",
        "gu": "Gujarati",
        "mr": "Marathi",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ja": "Japanese",
        "ko": "Korean",
        "zh-cn": "Chinese"
    }

    if detected_code:
        detected_name = language_names.get(
            detected_code,
            detected_code
        )

        st.info(f"🔍 Detected Language: **{detected_name}**")


# Select target language
target_language = st.selectbox(
    "Select target language:",
    list(languages.keys())
)


# Translate button
if st.button(" Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text first.")

    else:
        target_code = languages[target_language]

        with st.spinner("Translating..."):
            result = translate_text(
                text,
                target_code
            )

        st.subheader("Translation")
        st.success(result)


# Footer
st.divider()

st.caption(
    "AI Language Translator | Built with Python, Streamlit and Google Translator"
)
