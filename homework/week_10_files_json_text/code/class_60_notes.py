# Notes app mein ek note add karo aur ek keyword se search karo.
# Add a note in the Notes app and search for it using a keyword.



import json
from pathlib import Path
from datetime import datetime

NOTE_FILE = Path(__file__).parent / "notes.json"


# Load notes from JSON file
def load_notes():
    if NOTE_FILE.exists():
        try:
            with open(NOTE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data
                else:
                    return []

        except json.JSONDecodeError:
            return []

    return []


# Save notes to JSON file
def save_notes(notes):
    with open(NOTE_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)


# Add a new note
def save_note(note_text):
    notes = load_notes()

    new_note = {
        "note": note_text,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    notes.append(new_note)

    save_notes(notes)

    print("Note saved successfully!")


# Search notes
def search_notes(keyword):
    notes = load_notes()
    results = []

    for note in notes:

        # If note is a dictionary
        if isinstance(note, dict):

            # Try different possible keys safely
            note_text = (
                note.get("note")
                or note.get("text")
                or note.get("content")
                or note.get("message")
                or ""
            )

            if keyword.lower() in str(note_text).lower():
                results.append(note)

        # If note is directly a string
        elif isinstance(note, str):

            if keyword.lower() in note.lower():
                results.append(note)

    return results


# -----------------------------
# Main Program
# -----------------------------

save_note("Buy groceries")

results = search_notes("groceries")

print("\nSearch Results:")

if results:
    for note in results:
        print(note)
else:
    print("No notes found.")

    
