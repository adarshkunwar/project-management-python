import json
import tkinter as tk
from tkinter import messagebox

fileName = "hello.json"
running = True

try:
    with open(fileName, "r") as json_file:
        try:
            data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            data = []
except FileNotFoundError:
    data = []


def find_idea(data, idea):
    for item in data:
        if "idea" in item and item["idea"] == idea:
            return item
    return None


def add_idea():
    new_idea = entry.get()
    idea = find_idea(data, new_idea)
    if idea is None:
        data.append({"idea": new_idea, "choice": 1})
    else:
        idea["choice"] += 1
    with open(fileName, "w") as json_file:
        json.dump(data, json_file)
    entry.delete(0, tk.END)
    messagebox.showinfo("Idea Added", "Idea has been added successfully.")


def exit_program():
    global running
    running = False
    window.destroy()


window = tk.Tk()
window.title("Idea Management")
window.geometry("300x150")

label = tk.Label(window, text="Enter a new Idea:")
label.pack()

entry = tk.Entry(window)
entry.pack()

add_button = tk.Button(window, text="Add Idea", command=add_idea)
add_button.pack()

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

window.mainloop()
