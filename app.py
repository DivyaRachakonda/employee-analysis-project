import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string

# Download stopwords (run once)
nltk.download('stopwords')

# Preprocessing function
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in stop_words and word not in string.punctuation]
    return " ".join(words)

# Streamlit UI
st.title("📄 AI Resume Analyzer")
st.write("Compare your resume with a job description")

# Inputs
resume_text = st.text_area("Paste Your Resume")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_text and job_desc:
        # Preprocess text
        resume_clean = preprocess(resume_text)
        job_clean = preprocess(job_desc)

        # Vectorization
        cv = CountVectorizer()
        matrix = cv.fit_transform([resume_clean, job_clean])

        # Similarity
        similarity = cosine_similarity(matrix)[0][1]

        # Display result
        st.subheader("📊 Match Score")
        st.success(f"{round(similarity * 100, 2)} %")

        # Keyword comparison
        resume_words = set(resume_clean.split())
        job_words = set(job_clean.split())

        missing_skills = job_words - resume_words

        st.subheader("❌ Missing Keywords")
        st.write(", ".join(missing_skills) if missing_skills else "None 🎉")

    else:
        st.warning("Please enter both resume and job description")