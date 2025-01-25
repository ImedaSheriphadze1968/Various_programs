import json
from tkinter import messagebox

# ენის დატვირთვა
def load_language(language_code):
    try:
        with open(f'lang/{language_code}.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Language file not found: {language_code}.json")
        return {}

# UI განახლება
def update_ui(lang, title_label, tasks_label, distractions_label, hours_label, generate_button):
    title_label.config(text=lang.get("graphTitle", "Default Title"))
    tasks_label.config(text=lang.get("enterTasks", "Enter Tasks"))
    distractions_label.config(text=lang.get("enterDistractions", "Enter Distractions"))
    hours_label.config(text=lang.get("enterAvailableHours", "Enter Available Hours"))
    generate_button.config(text=lang.get("generateSchedule", "Generate Schedule"))
