🤖 AI-Based Resume Screening System

An AI-powered resume screening and candidate ranking system using Natural Language Processing (NLP), Transformer Embeddings, Semantic Similarity, and Explainable AI.

📌 Project Overview

Recruiters may need to evaluate a large number of resumes for a single job opening. Traditional keyword-based screening can miss relevant candidates when similar skills are described using different terminology.

This project proposes an AI-based approach that analyzes resumes against a job description, calculates semantic similarity, evaluates required skills, ranks candidates, and provides explainable insights.

🎯 Objectives

- Automatically extract text from candidate resumes.
- Analyze job descriptions using NLP.
- Generate semantic embeddings using a Transformer model.
- Calculate resume–job-description similarity.
- Evaluate required technical skills.
- Rank candidates according to their overall match.
- Identify matched and missing skills.
- Provide explainable candidate insights.
- Present results through an interactive Streamlit interface.

🏗️ System Architecture

                 ┌─────────────────────┐
                 │   Job Description   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Text Preprocessing │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Transformer Model   │
                 │ all-MiniLM-L6-v2    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Semantic Embeddings │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Similarity Matching  │
                 └──────────┬──────────┘
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
      Semantic Score                 Skill Matching
             │                             │
             └──────────────┬──────────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Candidate Ranking   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Explainable Results │
                 └─────────────────────┘

✨ Key Features

📄 Resume Processing

The system accepts PDF resumes and extracts their textual content automatically.

🧠 Transformer-Based Matching

The project uses the "all-MiniLM-L6-v2" Sentence Transformer model to generate semantic embeddings.

This allows the system to identify relationships between concepts even when exact keywords are not identical.

🔍 Semantic Similarity

Resume and job-description embeddings are compared using cosine similarity.

🛠️ Skill Matching

The system identifies technical skills appearing in both the resume and job description.

🏆 Candidate Ranking

Candidates are ranked according to a combined score based on semantic similarity and skill alignment.

💡 Explainable AI

Instead of returning only a score, the system provides:

- Matched skills
- Missing skills
- Score interpretation
- Candidate recommendation

🌐 Interactive Interface

The application is designed using Streamlit for an accessible web-based interface.

🖥️ Application Screenshots

Dashboard

"Dashboard" (image 1.jpeg)

Resume Screening

"Resume Screening" (image .jpeg)

Candidate Ranking

"Candidate Ranking" (image 3.jpeg)

Code and Results

"Code and Results" (image 5.jpeg)

🛠️ Technologies Used

Technology| Purpose
Python| Core programming language
Streamlit| Web application
Sentence Transformers| Semantic embeddings
scikit-learn| Similarity calculation
PyMuPDF| PDF text extraction
python-docx| DOCX processing
Pandas| Data processing
NumPy| Numerical computation
Plotly| Data visualization
GitHub| Version control and project hosting

📁 Project Structure

AI-Resume-Screening-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── document_parser.py
│   ├── preprocessing.py
│   ├── embeddings.py
│   ├── matcher.py
│   ├── ranking.py
│   └── explainability.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── resume_screening.png
│   ├── candidate_ranking.png
│   └── code_and_results.png
│
└── docs/
    └── project_report.pdf

⚙️ Processing Pipeline

Resume PDF
     ↓
Text Extraction
     ↓
Text Preprocessing
     ↓
Skill Extraction
     ↓
Transformer Embedding
     ↓
Cosine Similarity
     ↓
Skill Matching
     ↓
Weighted Final Score
     ↓
Candidate Ranking
     ↓
Explainable Results

📊 Scoring Approach

The project combines semantic similarity and skill alignment.

Final Score =
0.70 × Semantic Similarity
+
0.30 × Skill Match

The weighting is configurable and can be tuned using a labelled evaluation dataset.

«The displayed score represents system matching relevance and should not be interpreted as a hiring decision or model accuracy.»

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/AI-Resume-Screening-System.git

Move into the project directory:

cd AI-Resume-Screening-System

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

📄 Project Documentation

The complete major-project report is available here:

"docs/project_report.pdf"

The report contains:

- Problem statement
- Objectives
- System architecture
- Methodology
- Technology stack
- Evaluation plan
- Responsible AI considerations
- Development roadmap
- Future enhancements

⚠️ Responsible AI

This project is intended as a decision-support system, not an autonomous hiring system.

The ranking should be reviewed by a human decision-maker.

The system should not use protected characteristics or inappropriate personal information when evaluating candidates.

Sample or demonstration resumes should be synthetic, anonymized, or used with appropriate permission.

🔮 Future Enhancements

- Multilingual resume processing
- OCR for scanned resumes
- Advanced cross-encoder reranking
- Domain-specific model fine-tuning
- Skill ontology and taxonomy
- Docker deployment
- Cloud deployment
- Recruiter feedback integration
- Bias and fairness evaluation
- Advanced evaluation using Precision@K, Recall@K and NDCG

🎓 Academic Project

Project Title: AI-Based Resume Screening System

Domain: Artificial Intelligence / Machine Learning / Natural Language Processing

Application: Automated Resume Screening and Candidate Ranking

👨‍💻 Author

Sreedev D S 

Student | AI & Machine Learning Project

---
