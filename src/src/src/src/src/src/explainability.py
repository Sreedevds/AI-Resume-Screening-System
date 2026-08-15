def generate_explanation(
    candidate_name,
    final_score,
    matched_skills,
    missing_skills
):
    """
    Generate an explainable summary for a candidate.
    """

    explanation = {
        "Candidate": candidate_name,
        "Score": round(final_score, 2),
        "Matched Skills": matched_skills,
        "Missing Skills": missing_skills,
        "Recommendation": get_recommendation(
            final_score
        )
    }

    return explanation


def get_recommendation(score):
    """
    Convert the final score into a recommendation.
    """

    if score >= 85:
        return "Highly Recommended"

    elif score >= 70:
        return "Recommended"

    elif score >= 55:
        return "Needs Review"

    return "Low Match"


def generate_skill_summary(
    matched_skills,
    missing_skills
):
    """
    Generate a human-readable skill summary.
    """

    if matched_skills:

        matched_text = (
            "Matched skills: "
            + ", ".join(matched_skills)
            + "."
        )

    else:

        matched_text = (
            "No matching skills were detected."
        )

    if missing_skills:

        missing_text = (
            "Potential skill gaps: "
            + ", ".join(missing_skills)
            + "."
        )

    else:

        missing_text = (
            "No major skill gaps were detected."
        )

    return (
        matched_text
        + " "
        + missing_text
    )


def generate_candidate_report(
    candidate_name,
    final_score,
    matched_skills,
    missing_skills
):
    """
    Generate a complete candidate explanation.
    """

    recommendation = get_recommendation(
        final_score
    )

    skill_summary = generate_skill_summary(
        matched_skills,
        missing_skills
    )

    return {
        "candidate": candidate_name,
        "score": round(final_score, 2),
        "recommendation": recommendation,
        "skill_summary": skill_summary
    }
