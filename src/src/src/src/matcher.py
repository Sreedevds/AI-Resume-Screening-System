from sklearn.metrics.pairwise import cosine_similarity

from .embeddings import generate_embedding
from .preprocessing import normalize_text


def calculate_semantic_similarity(
    resume_text,
    job_description
):
    """
    Calculate semantic similarity between
    a resume and a job description.
    """

    resume_text = normalize_text(
        resume_text
    )

    job_description = normalize_text(
        job_description
    )

    resume_embedding = generate_embedding(
        resume_text
    )

    job_embedding = generate_embedding(
        job_description
    )

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    return float(similarity)


def calculate_skill_match(
    resume_skills,
    job_skills
):
    """
    Calculate the percentage of required
    job skills found in the resume.
    """

    resume_skills = {
        skill.lower()
        for skill in resume_skills
    }

    job_skills = {
        skill.lower()
        for skill in job_skills
    }

    if not job_skills:
        return 0.0

    matched_skills = (
        resume_skills & job_skills
    )

    score = (
        len(matched_skills)
        / len(job_skills)
    )

    return float(score)


def get_matched_skills(
    resume_skills,
    job_skills
):
    """
    Return skills present in both
    the resume and job description.
    """

    resume_skills = {
        skill.lower()
        for skill in resume_skills
    }

    job_skills = {
        skill.lower()
        for skill in job_skills
    }

    return sorted(
        resume_skills & job_skills
    )


def get_missing_skills(
    resume_skills,
    job_skills
):
    """
    Return required skills that were
    not detected in the resume.
    """

    resume_skills = {
        skill.lower()
        for skill in resume_skills
    }

    job_skills = {
        skill.lower()
        for skill in job_skills
    }

    return sorted(
        job_skills - resume_skills
    )


def calculate_final_score(
    semantic_score,
    skill_score,
    semantic_weight=0.70,
    skill_weight=0.30
):
    """
    Combine semantic similarity and skill
    matching into one final score.
    """

    final_score = (
        semantic_weight * semantic_score
        +
        skill_weight * skill_score
    )

    return float(final_score)
