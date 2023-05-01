import json
import os
def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f)
    print("Saved {} notes".format(len(notes)))

def load_notes():
    if not os.path.exists("notes.json"):
        with open("notes.json", "w") as f:
            json.dump([], f)
    with open("notes.json", "r") as f:
        notes = json.load(f)
    count_notes = len(notes)
    print("Downloaded {} notes".format(count_notes))
    return notes

def edit_note(notes, title):
    for note in notes:
        if note["title"] == title:
            new_title = input("Enter a new name: ")
            new_text = input("Enter new text: ")
            new_tags = input("Enter tags (through comma): ")
            while "," not in new_tags:
                print("Error: Tags must be comma separated.")
                new_tags = input("Enter tags (through comma): ")
            new_tags = [tag.strip() for tag in new_tags.split(",")]
            note["title"] = new_title
            note["text"] = new_text
            note["tags"] = new_tags
            save_notes(notes)
            print("The note has been edited successfully")
            return
    print("No note with this name was found.")

def delete_note(notes, title):
    for note in notes:
        if note["title"] == title:
            notes.remove(note)
            save_notes(notes)
            print("Note deleted successfully")
            return
    print("No note with this name was found.")

def search_notes_by_tags(notes, tags):
    result_notes = []
    for note in notes:
        if set(tags).issubset(set(note["tags"])):
            result_notes.append(note)
    return result_notes

def sort_notes_by_tags(notes):
    sorted_notes = sorted(notes, key=lambda x: x["tags"])
    return sorted_notes

def main():
    notes = load_notes()
    while True:
        print("1 - Add a note")
        print("2 - Edit note")
        print("3 - Delete note")
        print("4 - Search by tags")
        print("5 - Sort by tags")
        print("6 - Exit")
        choice = input("Enter the option number: ")
        if choice == "1":
            title = input("Enter a name: ")
            text = input("Enter the text: ")
            tags = input("Enter tags (through comma): ").split(",")
            new_note = {"title": title, "text": text, "tags": [tag.strip() for tag in tags]}
            notes.append(new_note)
            save_notes(notes)
        elif choice == "2":
            title = input("Enter a name for the note: ")
            edit_note(notes, title)
        elif choice == "3":
            title = input("Enter a name for the note: ")
            delete_note(notes, title)
        elif choice == "4":
            tags = input("Enter tags (through comma): ").split(",")
            result_notes = search_notes_by_tags(notes, [tag.strip() for tag in tags])
            print("Notes found: ", len(result_notes))
            for note in result_notes:
                print("Name: ", note["title"])
                print("Text: ", note["text"])
                print("Tags: ", ", ".join(note["tags"]))
        elif choice == "5":
            sorted_notes = sort_notes_by_tags(notes)
            for note in sorted_notes:
                print("Name: ", note["title"])
                print("Text: ", note["text"])
                print("Tags: ", ", ".join(note["tags"]))
        elif choice == "6":
            break
        else:
            print("Wrong choice. Try again.")
            






                