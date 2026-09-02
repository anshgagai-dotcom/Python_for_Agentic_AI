
import json
import keyword
import logging
import re

from datetime import datetime
from pathlib import Path
from time import asctime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

NOTE_FILE = Path("notes.json")

def load_notes():
    if not NOTE_FILE.exists():
        logging.warning(f"Note file {NOTE_FILE} not found")
        return []
    with open(NOTE_FILE, "r", encoding="utf-8") as f:
        logging.info(f"Note file {NOTE_FILE} loaded")
        return json.load(f)

def save_notes(text: str)-> None:
    notes = load_notes()
    note = {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "text": text}
    notes.append(note)

    with open(NOTE_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)
    logging.info(f"Note saved to {NOTE_FILE}")    


def search_notes(keyword: str)-> list:
    notes = load_notes()

   # matches = []
   # for note in notes:

      #  text = note["text"]

      #  match = re.search(keyword, text, re.IGNORECASE)
       # matches.append(match)

    return [ note for note in notes if re.search(keyword, note["text"], re.IGNORECASE)]
        

if __name__ == "__main__":
    save_notes("This is my daily routing notebook")
    save_notes("My mobile nimber is 7078743687")
    save_notes("This is my personal notebook so if you opended then please close it")

    search_results = search_notes("7078743687")
    print(search_results)
    
  



