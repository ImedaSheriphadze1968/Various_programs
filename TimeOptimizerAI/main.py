from tkinter import *
from tkinter import messagebox
from utils import load_language, update_ui
from Graph import generate_graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # საჭირო იმპორტი

# ძირითადი ფანჯარა
root = Tk()
root.title("TimeOptimizer AI")
root.geometry("900x600")

# ენის დატვირთვა
lang = load_language("en")  # ნაგულისხმევი ენა: English

# UI ელემენტები
title_label = Label(root, text=lang.get("graphTitle", "Default Title"), font=("Arial", 18, "bold"))
title_label.pack(pady=10)

tasks_label = Label(root, text=lang.get("enterTasks", "Enter Tasks"))
tasks_label.pack()
tasks_entry = Entry(root)
tasks_entry.pack()

distractions_label = Label(root, text=lang.get("enterDistractions", "Enter Distractions"))
distractions_label.pack()
distractions_entry = Entry(root)
distractions_entry.pack()

hours_label = Label(root, text=lang.get("enterAvailableHours", "Enter Available Hours"))
hours_label.pack()
hours_entry = Entry(root)
hours_entry.pack()

# ღილაკი გრაფიკის გენერაციისთვის
def generate_schedule():
    try:
        tasks = tasks_entry.get().split(",")  # დავალებების შეყვანა
        hours = list(map(int, hours_entry.get().split()))  # საათების შეყვანა
        distractions = distractions_entry.get().split(",")  # ყურადღების გადატანა
        fig, ax = generate_graph(tasks, hours, distractions)

        # Matplotlib გრაფიკის ჩასმა Tkinter ფანჯარაში
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

generate_button = Button(root, text=lang.get("generateSchedule", "Generate Schedule"), command=generate_schedule)
generate_button.pack(pady=10)

# ენების გადამრთველი მენიუ
def switch_language(lang_code):
    global lang
    lang = load_language(lang_code)
    update_ui(lang, title_label, tasks_label, distractions_label, hours_label, generate_button)

language_menu = Menubutton(root, text=lang.get("selectLanguage", "Language"), relief=RAISED, font=("Arial", 12))
language_menu.menu = Menu(language_menu, tearoff=0)
language_menu["menu"] = language_menu.menu

languages = {"English": "en", "ქართული": "ka", "Русский": "ru", "Deutsch": "de", "Français": "fr"}
for name, code in languages.items():
    language_menu.menu.add_command(label=name, command=lambda c=code: switch_language(c))

language_menu.pack(pady=20)

root.mainloop()
