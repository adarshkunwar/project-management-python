import json
import tkinter as tk
import random
from tkinter import messagebox

def load_data(file_name):
    try:
        with open(file_name, "r") as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                data = []
    except FileNotFoundError:
        data = []
    return data

def save_data(file_name, data):
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)

def find_idea(data, idea):
    for item in data:
        if "idea" in item and item["idea"] == idea:
            return item
    return None

def add_idea():
    global entry
    new_idea = entry.get()
    idea = find_idea(data, new_idea)
    if idea is None:
        data.append({"idea": new_idea, "choice": 1})
    else:
        idea["choice"] += 1
    save_data(file_name, data)
    entry.delete(0, tk.END)
    messagebox.showinfo("Idea Added", "Idea has been added successfully.")

def exit_program():
    global running
    running = False
    window.destroy()

def generate_idea():
    if not data:
        messagebox.showinfo("No Ideas", "No ideas available. Please add some ideas.")
        return
    
    # Calculate the total choices
    total_choices = sum(item["choice"] for item in data)
    
    # Generate a random number between 0 and the total choices
    random_choice = random.randint(0, total_choices - 1)
    
    # Select the idea based on the random choice
    cumulative_choice = 0
    selected_idea = None
    for item in data:
        cumulative_choice += item["choice"]
        if random_choice < cumulative_choice:
            selected_idea = item["idea"]
            break
    
    if selected_idea:
        messagebox.showinfo("Random Idea", f"The randomly generated idea is:\n\n{selected_idea}")
    else:
        messagebox.showinfo("Random Idea", "Failed to generate a random idea.")

def create_gui(window):
    global entry
    window.title("Idea Generator App")

    title_label = tk.Label(window, text="Idea Generator App", font=("Helvetica", 20))
    title_label.pack(pady=10)

    ideas_frame = tk.Frame(window)
    ideas_frame.pack(fill=tk.BOTH, expand=True)

    ideas_label = tk.Label(ideas_frame, text="New Ideas", font=("Helvetica", 16))
    ideas_label.pack(pady=5)

    idea_listbox = tk.Listbox(ideas_frame, font=("Helvetica", 12))
    idea_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    for item in data:
        idea_listbox.insert(tk.END, item["idea"])

    input_frame = tk.Frame(window)
    input_frame.pack(pady=10)

    label = tk.Label(input_frame, text="Enter a new Idea:", font=("Helvetica", 12))
    label.pack(side=tk.LEFT)

    entry = tk.Entry(input_frame, font=("Helvetica", 12))
    entry.pack(side=tk.LEFT)

    add_button = tk.Button(window, text="Add Idea", font=("Helvetica", 12), command=add_idea)
    add_button.pack(pady=5)

    generate_frame = tk.Frame(window)
    generate_frame.pack(pady=20)

    generate_button = tk.Button(generate_frame, text="Generate an idea", font=("Helvetica", 16), bg="red", fg="white", width=15, height=3, command=generate_idea)
    generate_button.pack()

    exit_button = tk.Button(window, text="Exit", font=("Helvetica", 12), command=exit_program)
    exit_button.pack(pady=10)

    window.geometry("400x600")

# Main program
file_name = "hello.json"
data = load_data(file_name)
running = True

window = tk.Tk()
create_gui(window)
window.mainloop()
