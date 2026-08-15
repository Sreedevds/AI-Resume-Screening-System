import pandas as pd


def rank_candidates(results):
    """
    Sort candidates by their final matching score
    from highest to lowest.
    """

    if not results:
        return pd.DataFrame()

    dataframe = pd.DataFrame(results)

    if "Final Score" not in dataframe.columns:
        raise ValueError(
            "Results must contain 'Final Score'."
        )

    dataframe = dataframe.sort_values(
        by="Final Score",
        ascending=False
    ).reset_index(drop=True)

    dataframe.insert(
        0,
        "Rank",
        range(1, len(dataframe) + 1)
    )

    return dataframe


def get_top_candidates(
    dataframe,
    top_k=5
):
    """
    Return the top K candidates.
    """

    if dataframe.empty:
        return dataframe

    return dataframe.head(top_k)


def get_candidate_category(score):
    """
    Convert a numerical score into a simple
    interpretation category.
    """

    if score >= 85:
        return "Excellent Match"

    if score >= 70:
        return "Strong Match"

    if score >= 55:
        return "Moderate Match"

    return "Low Match"
