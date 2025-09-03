# Flashcards CLI (CS50 Final Project)
#### Video Demo:  <VIDEO_URL_HERE>
#### Description:

This project is a command-line based flashcard learning tool written in Python.
It is my final project for Harvard’s CS50P (CS50’s Introduction to Programming with Python).

The purpose of the project is to help users create, review, and retain knowledge with a spaced-repetition system similar to Anki or SuperMemo, but in a lightweight, terminal-based format. Instead of a graphical interface, the project is fully controlled through command-line arguments, making it fast and scriptable.

---

### Features

- **Add Flashcards**
  Users can add new cards directly from the command line by specifying a question and answer. Cards are stored in JSON format for persistence between runs.

- **Review Flashcards**
  The program selects due cards based on spaced-repetition scheduling. Users mark answers as “good” or “again,” and the interval adjusts accordingly, so easier cards appear less frequently over time.

- **List Cards**
  All saved cards can be listed in the terminal, showing questions, answers, and scheduling information (interval, ease factor, next review date).

- **JSON Storage**
  Cards are saved in a file (`deck.json` by default). This ensures that decks persist between sessions and can be backed up or shared.

---

### File Structure

- **project.py**
  The main program. Contains:
  - `main()` → Entry point for the CLI. Parses arguments and calls the relevant functions.
  - `add_card()` → Adds a new card to the deck.
  - `review_cards()` → Reviews due cards using spaced repetition.
  - `list_cards()` → Displays all cards in the deck.
  - `load_deck()` / `save_deck()` → Handles JSON storage.

- **test_project.py**
  Contains tests for at least three core functions using `pytest`. For example:
  - `test_add_card()` ensures cards are added correctly.
  - `test_load_and_save_deck()` checks JSON persistence.
  - `test_review_logic()` verifies spaced-repetition logic.

- **requirements.txt**
  Lists required Python packages. In this case, only `pytest` is strictly required.

- **README.md**
  The file you are reading now. Explains the project, design decisions, and instructions for running it.

---

### Design Choices

I chose a command-line interface rather than a web or GUI approach to emphasize Python’s standard libraries, argument parsing, and file handling.
Using JSON for storage makes the project simple but extensible — cards can be easily exported, modified, or shared.

I also implemented a basic spaced-repetition algorithm (increasing intervals and adjusting ease factor) to make the tool genuinely useful for long-term learning, not just a random quiz app.

---

### How to Run


1. Install dependencies:
   ```bash
   pip install -r requirements.txt
```
2. Add a flashcard
```bash
   python project.py add "What is 2+2?" "4"
```
3. Review due cards
    ```bash
   python project.py review
```
4. List all cards
   ```bash
   python project.py list
```


