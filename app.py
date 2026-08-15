import streamlit as st
import pandas as pd

from src.document_parser import extract_pdf_text
from src.preprocessing import normalize_text
from src.matcher import (
    calculate_semantic_similarity,
    calculate_skill_match,
    get_matched_skills,
    get_missing_skills,
    calculate_final_score
)
from src.ranking import (
    rank_candidates,
    get_candidate_category
)
from src.explainability import (
    generate_candidate_report
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f7f8fc;
    }

    .result-card {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        margin-bottom: 15px;
        border-left: 5px solid #6c63ff;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    }

    .metric-card {
        padding: 15px;
        border-radius: 10px;
        background-color: white;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.title(
    "🤖 AI-Based Resume Screening System"
)

st.write(
    "AI-powered resume screening using "
    "NLP, transformer embeddings and semantic matching."
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ System Information")

    st.write(
        """
        **AI Model**

        Sentence Transformer  
        `all-MiniLM-L6-v2`
        """
    )

    st.write(
        """
        **Matching**

        • Semantic similarity  
        • Skill matching  
        • Weighted scoring
        """
    )

    st.info(
        "This application is designed as a "
        "decision-support tool. Final candidate "
        "decisions should be reviewed by a human."
    )


# =========================================================
# DASHBOARD METRICS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "AI Model",
        "MiniLM"
    )

with col2:

    st.metric(
        "Matching",
        "Semantic + Skills"
    )

with col3:

    st.metric(
        "Ranking",
        "Automated"
    )


st.markdown("---")


# =========================================================
# JOB DESCRIPTION
# =========================================================

st.header(
    "📋 Job Description"
)

job_description = st.text_area(

    "Paste the job description below:",

    height=220,

    placeholder="""
Example:

We are looking for a Machine Learning Engineer
with experience in Python, SQL, machine learning,
deep learning and NLP.

Candidates should have experience developing
AI applications and working with data.
"""
)


# =========================================================
# RESUME UPLOAD
# =========================================================

st.header(
    "📄 Upload Candidate Resumes"
)

uploaded_resumes = st.file_uploader(

    "Upload PDF resumes",

    type=["pdf"],

    accept_multiple_files=True
)


# =========================================================
# SCREEN BUTTON
# =========================================================

if st.button(
    "🚀 Screen Resumes",
    use_container_width=True
):

    if not job_description:

        st.warning(
            "Please enter a job description first."
        )

        st.stop()

    if not uploaded_resumes:

        st.warning(
            "Please upload at least one resume."
        )

        st.stop()


    # -----------------------------------------------------
    # PROCESS JOB DESCRIPTION
    # -----------------------------------------------------

    job_text = normalize_text(
        job_description
    )


    results = []


    # -----------------------------------------------------
    # PROCESS EACH RESUME
    # -----------------------------------------------------

    with st.spinner(
        "Analyzing resumes using AI..."
    ):

        for uploaded_file in uploaded_resumes:

            # Extract text
            resume_text = extract_pdf_text(
                uploaded_file
            )

            # Normalize text
            resume_text = normalize_text(
                resume_text
            )


            # -------------------------------------------------
            # SKILL EXTRACTION
            # -------------------------------------------------

            # Skills used by the project
            skills = [

                "python",
                "java",
                "c++",
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


            resume_skills = [

                skill

                for skill in skills

                if skill in resume_text
            ]


            job_skills = [

                skill

                for skill in skills

                if skill in job_text
            ]


            # -------------------------------------------------
            # SEMANTIC SCORE
            # -------------------------------------------------

            semantic_score = (
                calculate_semantic_similarity(
                    resume_text,
                    job_text
                )
            )


            # -------------------------------------------------
            # SKILL SCORE
            # -------------------------------------------------

            skill_score = calculate_skill_match(

                resume_skills,

                job_skills
            )


            # -------------------------------------------------
            # MATCHED / MISSING SKILLS
            # -------------------------------------------------

            matched_skills = get_matched_skills(

                resume_skills,

                job_skills
            )


            missing_skills = get_missing_skills(

                resume_skills,

                job_skills
            )


            # -------------------------------------------------
            # FINAL SCORE
            # -------------------------------------------------

            final_score = calculate_final_score(

                semantic_score,

                skill_score
            )


            results.append({

                "Candidate":
                    uploaded_file.name,

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
                        matched_skills
                    ),

                "Missing Skills":
                    ", ".join(
                        missing_skills
                    )
            })


    # =====================================================
    # RANK CANDIDATES
    # =====================================================

    ranked_results = rank_candidates(
        results
    )


    st.success(
        "Resume screening completed successfully!"
    )


    # =====================================================
    # RESULTS
    # =====================================================

    st.header(
        "🏆 Candidate Ranking"
    )

    display_columns = [

        "Rank",
        "Candidate",
        "Semantic Score",
        "Skill Score",
        "Final Score"
    ]


    st.dataframe(

        ranked_results[
            display_columns
        ],

        use_container_width=True,

        hide_index=True
    )


    # =====================================================
    # SCORE CHART
    # =====================================================

    st.header(
        "📊 Candidate Score Analysis"
    )

    chart_data = (

        ranked_results[
            [
                "Candidate",
                "Final Score"
            ]
        ]

        .set_index(
            "Candidate"
        )
    )


    st.bar_chart(
        chart_data
    )


    # =====================================================
    # TOP CANDIDATE
    # =====================================================

    st.header(
        "🥇 Top Candidate"
    )


    top_candidate = ranked_results.iloc[0]


    category = get_candidate_category(

        top_candidate[
            "Final Score"
        ]
    )


    st.markdown(

        f"""
        <div class="result-card">

        <h2>
        {top_candidate["Candidate"]}
        </h2>

        <h1>
        {top_candidate["Final Score"]}%
        </h1>

        <b>{category}</b>

        <br><br>

        <b>Semantic Score:</b>
        {top_candidate["Semantic Score"]}%

        <br>

        <b>Skill Score:</b>
        {top_candidate["Skill Score"]}%

        </div>
        """,

        unsafe_allow_html=True
    )


    # =====================================================
    # EXPLAINABLE RESULTS
    # =====================================================

    st.header(
        "💡 Explainable Candidate Insights"
    )


    for _, candidate in ranked_results.iterrows():

        candidate_report = (
            generate_candidate_report(

                candidate["Candidate"],

                candidate["Final Score"],

                candidate[
                    "Matched Skills"
                ].split(", ")
                if candidate[
                    "Matched Skills"
                ]
                else [],

                candidate[
                    "Missing Skills"
                ].split(", ")
                if candidate[
                    "Missing Skills"
                ]
                else []
            )
        )


        with st.expander(

            f'#{int(candidate["Rank"])} '
            f'{candidate["Candidate"]} — '
            f'{candidate["Final Score"]}%'
        ):

            st.write(
                "**Recommendation:**",
                candidate_report[
                    "recommendation"
                ]
            )


            st.write(
                candidate_report[
                    "skill_summary"
                ]
            )


    # =====================================================
    # DOWNLOAD RESULTS
    # =====================================================

    st.header(
        "📥 Export Results"
    )


    csv = ranked_results.to_csv(
        index=False
    )


    st.download_button(

        label="Download Screening Results",

        data=csv,

        file_name=
        "resume_screening_results.csv",

        mime="text/csv",

        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "AI-Based Resume Screening System | "
    "NLP + Transformer Embeddings | Major Project"
)
