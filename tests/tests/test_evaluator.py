
import pytest

from evaluator import evaluate_responses


def test_response_a_wins():
    result = evaluate_responses(
        "Accurate answer",
        "Incorrect answer",
        9,
        4
    )

    assert result["winner"] == "Response A"


def test_response_b_wins():
    result = evaluate_responses(
        "First answer",
        "Better answer",
        5,
        9
    )

    assert result["winner"] == "Response B"


def test_equal_scores():
    result = evaluate_responses(
        "Answer A",
        "Answer B",
        7,
        7
    )

    assert result["winner"] == "Tie"


def test_empty_response_is_rejected():
    with pytest.raises(ValueError):
        evaluate_responses("", "Answer B", 5, 8)


def test_invalid_score_is_rejected():
    with pytest.raises(ValueError):
        evaluate_responses("Answer A", "Answer B", 11, 5)
