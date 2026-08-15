import streamlit as st
import fitz
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f7f8fc;
}

.metric-card {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

.result-card {
    padding: 18px;
    border-radius: 12px;
    background-color: white;
    margin-bottom: 15px;
    border-left: 5px solid #6c63ff;
}

h1 {
    color: #25234a;
}

h2 {
    color: #34315e;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# LOAD TRANSFORMER MODEL
# ---------------------------------------------------------

@st.cache_resource
def load_model():

    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


# ---------------------------------------------------------
# PDF TEXT EXTRACTION
# ---------------------------------------------------------

def extract_pdf_text(uploaded_file):

    document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


# ---------------------------------------------------------
# TEXT PREPROCESSING
# ---------------------------------------------------------

def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()


# ---------------------------------------------------------
# SKILL EXTRACTION
# ---------------------------------------------------------

SKILLS = [

    "python",
    "java",
    "c++",
    "c",
    "javascript",
    "typescript",
    "sql",
    "html",
    "css",
    "react",
    "node.js",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "natural language processing",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "data science",
    "computer vision",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "mongodb",
    "mysql",
    "postgresql",
    "excel"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text:

            found_skills.append(skill)

    return found_skills


# ---------------------------------------------------------
# SEMANTIC SIMILARITY
# ---------------------------------------------------------

def calculate_similarity(resume_text, job_text):

    embeddings = model.encode(
        [
            resume_text,
            job_text
        ]
    )

    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(score)


# ---------------------------------------------------------
# SCREEN RESUMES
# ---------------------------------------------------------

def screen_resumes(resumes, job_description):

    results = []

    job_clean = preprocess_text(job_description)

    job_skills = set(
        extract_skills(job_clean)
    )

    for resume_name, resume_text in resumes:

        clean_resume = preprocess_text(
            resume_text
        )

        semantic_score = calculate_similarity(
            clean_resume,
            job_clean
        )

        resume_skills = set(
            extract_skills(clean_resume)
        )

        matched_skills = (
            job_skills &
            resume_skills
        )

        missing_skills = (
            job_skills -
            resume_skills
        )

        if len(job_skills) > 0:

            skill_score = (
                len(matched_skills) /
                len(job_skills)
            )

        else:

            skill_score = 0

        final_score = (

            0.70 * semantic_score +

            0.30 * skill_score

        )

        results.append({

            "Candidate": resume_name,

            "Semantic Score":
                round(
                    semantic_score * 100,
                    2
                ),

            "Skill Score":
                round(
                    skill_score * 100,
                    2
                ),

            "Final Score":
                round(
                    final_score * 100,
                    2
                ),

            "Matched Skills":
                ", ".join(
                    sorted(
                        matched_skills
                    )
                ),

            "Missing Skills":
                ", ".join(
                    sorted(
                        missing_skills
                    )
                )
        })

    results.sort(
        key=lambda x:
        x["Final Score"],
        reverse=True
    )

    return results


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.title("🤖 AI Resume Screening")

    st.markdown("---")

    st.markdown(
        """
        ### Navigation

        🏠 Dashboard

        📄 Resume Screening

        📊 Candidate Ranking

        💡 Explainable Results
        """
    )

    st.markdown("---")

    st.info(
        "This system uses NLP and transformer embeddings to compare resumes with job descriptions."
    )


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------

st.title(
    "🤖 AI-Based Resume Screening System"
)

st.write(
    "Automatically analyze resumes, compare them with a job description, "
    "and rank candidates using semantic similarity."
)


# ---------------------------------------------------------
# DASHBOARD METRICS
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "AI Model",
        "MiniLM"
    )

with col2:

    st.metric(
        "Matching Method",
        "Semantic + Skills"
    )

with col3:

    st.metric(
        "Ranking",
        "Automated"
    )


st.markdown("---")


# ---------------------------------------------------------
# JOB DESCRIPTION
# ---------------------------------------------------------

st.header(
    "📋 Job Description"
)

job_description = st.text_area(

    "Paste the job description here:",

    height=220,

    placeholder=
    """
    Example:

    We are looking for a Machine Learning Engineer
    with experience in Python, SQL, NLP, machine learning
    and deep learning.

    Candidates should have strong programming skills
    and experience developing AI applications.
    """
)


# ---------------------------------------------------------
# RESUME UPLOAD
# ---------------------------------------------------------

st.header(
    "📄 Upload Resumes"
)

uploaded_resumes = st.file_uploader(

    "Upload candidate resumes in PDF format",

    type=["pdf"],

    accept_multiple_files=True
)


# ---------------------------------------------------------
# PROCESSING
# ---------------------------------------------------------

if st.button(
    "🚀 Screen Resumes",
    use_container_width=True
):

    if not job_description:

        st.warning(
            "Please enter a job description."
        )

    elif not uploaded_resumes:

        st.warning(
            "Please upload at least one resume."
        )

    else:

        with st.spinner(
            "Analyzing resumes using AI..."
        ):

            resumes = []

            for uploaded_file in uploaded_resumes:

                text = extract_pdf_text(
                    uploaded_file
                )

                resumes.append(
                    (
                        uploaded_file.name,
                        text
                    )
                )

            results = screen_resumes(
                resumes,
                job_description
            )

        st.success(
            "Resume screening completed successfully!"
        )


        # -------------------------------------------------
        # RESULTS
        # -------------------------------------------------

        st.header(
            "🏆 Candidate Ranking"
        )

        dataframe = pd.DataFrame(
            results
        )

        st.dataframe(
            dataframe,
            use_container_width=True,
            hide_index=True
        )


        # -------------------------------------------------
        # TOP CANDIDATE
        # -------------------------------------------------

        top_candidate = results[0]

        st.markdown("---")

        st.header(
            "🥇 Top Candidate"
        )

        st.markdown(
            f"""
            <div class="result-card">

            <h3>{top_candidate["Candidate"]}</h3>

            <h2>
            {top_candidate["Final Score"]}%
            Match
            </h2>

            <b>Semantic Score:</b>
            {top_candidate["Semantic Score"]}%<br>

            <b>Skill Score:</b>
            {top_candidate["Skill Score"]}%<br><br>

            <b>Matched Skills:</b><br>
            {top_candidate["Matched Skills"] or "None detected"}

            <br><br>

            <b>Missing Skills:</b><br>
            {top_candidate["Missing Skills"] or "None detected"}

            </div>
            """,
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # SCORE CHART
        # -------------------------------------------------

        st.header(
            "📊 Candidate Score Analysis"
        )

        chart_data = dataframe[
            [
                "Candidate",
                "Final Score"
            ]
        ].set_index(
            "Candidate"
        )

        st.bar_chart(
            chart_data
        )


        # -------------------------------------------------
        # DOWNLOAD RESULTS
        # -------------------------------------------------

        csv = dataframe.to_csv(
            index=False
        )

        st.download_button(

            label="⬇️ Download Screening Results",

            data=csv,

            file_name=
            "resume_screening_results.csv",

            mime="text/csv",

            use_container_width=True
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.caption(
    "AI-Based Resume Screening System | NLP + Transformer Embeddings | Major Project"
)
