
def evaluate_responses(
    response_a,
    response_b,
    score_a,
    score_b
):
    """Compare two AI-generated responses."""

    if not response_a.strip():
        raise ValueError("Response A cannot be empty.")

    if not response_b.strip():
        raise ValueError("Response B cannot be empty.")

    if not 0 <= score_a <= 10:
        raise ValueError("Score A must be between 0 and 10.")

    if not 0 <= score_b <= 10:
        raise ValueError("Score B must be between 0 and 10.")

    if score_a > score_b:
        winner = "Response A"
    elif score_b > score_a:
        winner = "Response B"
    else:
        winner = "Tie"

    return {
        "winner": winner,
        "score_a": score_a,
        "score_b": score_b,
        "score_difference": abs(score_a - score_b)
    }
