import json
import os

DB_FILE = "data.json"

def read_db():
    # If the file doesn't exist or is empty, create a default structure
    if not os.path.exists(DB_FILE) or os.path.getsize(DB_FILE) == 0:
        db = {
            "doctors": [],
            "patients": [],
            "appointments": [],
            "next_ids": {"doctor": 0, "patient": 0, "appointment": 0}
        }
        write_db(db)
        return db

    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)
