import json
from datetime import datetime, timedelta

DECK_FILE = "deck.json"


def main():
    """
    CLI interface:
    - python project.py add "question" "answer"
    - python project.py review
    """
    import sys

    if len(sys.argv) < 2:
        print("Usage: python project.py [add|review|list]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 4:
        q, a = sys.argv[2], sys.argv[3]
        card = create_card(q, a)
        deck = load_deck(DECK_FILE)
        deck.append(card)
        save_deck(DECK_FILE, deck)
        print(f"Added card: {q} -> {a}")

    elif command == "review":
        deck = load_deck(DECK_FILE)
        today = datetime.now().strftime("%Y-%m-%d")
        due = due_cards(deck, today)

        if not due:
            print("No cards due today.")
            return

        for card in due:
            print(f"Q: {card['question']}")
            input("Press Enter to see the answer...")
            print(f"A: {card['answer']}")
            correct = input("Did you get it right? (y/n): ").lower().startswith("y")
            updated = schedule_next(card, correct)
            # replace old card in deck
            idx = deck.index(card)
            deck[idx] = updated

        save_deck(DECK_FILE, deck)

    elif command == "list":
        deck = load_deck(DECK_FILE)
        print(f"{len(deck)} cards in deck:")
        for c in deck:
            print(f"- {c['question']} (next review {c['next_review']})")

    else:
        print("Invalid command or arguments.")


def create_card(question: str, answer: str) -> dict:
    """Return a new flashcard dict with scheduling metadata."""
    return {
        "question": question,
        "answer": answer,
        "interval": 1,  # days
        "ease": 2.5,
        "next_review": datetime.now().strftime("%Y-%m-%d"),
    }


def load_deck(path: str) -> list[dict]:
    """Load deck from JSON file, or return empty if not exists."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_deck(path: str, deck: list[dict]):
    """Save deck to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(deck, f, indent=2)


def schedule_next(card: dict, correct: bool) -> dict:
    """Update scheduling metadata depending on correctness."""
    if correct:
        # Increase interval exponentially by ease
        card["interval"] = int(card["interval"] * card["ease"])
        card["ease"] = min(card["ease"] + 0.1, 3.0)
    else:
        # Reset interval and reduce ease
        card["interval"] = 1
        card["ease"] = max(card["ease"] - 0.2, 1.3)

    next_date = datetime.now() + timedelta(days=card["interval"])
    card["next_review"] = next_date.strftime("%Y-%m-%d")
    return card


def due_cards(deck: list[dict], date: str) -> list[dict]:
    """Return all cards due on or before given date (YYYY-MM-DD)."""
    today = datetime.strptime(date, "%Y-%m-%d")
    return [c for c in deck if datetime.strptime(c["next_review"], "%Y-%m-%d") <= today]


if __name__ == "__main__":
    main()
