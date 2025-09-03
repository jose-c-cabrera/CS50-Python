import pytest
from project import create_card, schedule_next, due_cards


def test_create_card():
    card = create_card("Q1", "A1")
    assert card["question"] == "Q1"
    assert card["answer"] == "A1"
    assert card["interval"] == 1
    assert "next_review" in card


def test_schedule_next_correct():
    card = create_card("Q2", "A2")
    updated = schedule_next(card.copy(), True)
    assert updated["interval"] >= 1
    assert updated["ease"] > 2.4


def test_schedule_next_incorrect():
    card = create_card("Q3", "A3")
    updated = schedule_next(card.copy(), False)
    assert updated["interval"] == 1
    assert updated["ease"] < 2.5


def test_due_cards():
    card = create_card("Q4", "A4")
    # Card is due today
    due = due_cards([card], card["next_review"])
    assert card in due
