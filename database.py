import json
from pathlib import Path

DB_FILE = Path("chores_data.json")

def load_data():
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {"roommates": [], "chores": [], "assignments": {}}

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def add_roommate(name):
    data = load_data()
    if name not in data["roommates"]:
        data["roommates"].append(name)
        save_data(data)

def add_chore(chore):
    data = load_data()
    if chore not in data["chores"]:
        data["chores"].append(chore)
        save_data(data)

def get_roommates():
    return load_data()["roommates"]

def get_chores():
    return load_data()["chores"]

def save_assignments(assignments):
    data = load_data()
    data["assignments"] = assignments
    save_data(data)

def get_assignments():
    return load_data()["assignments"]
