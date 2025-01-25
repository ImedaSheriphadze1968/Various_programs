import tkinter as tk
from data.preprocess import preprocess_data
from models.neural_network import build_model, train_model
from utils.recommendations import recommend_improvements
from utils.file_operations import save_results

# ფუნქცია, რომელიც აჩენს GUI ფანჯარას
def start_gui():
    window = tk.Tk()
    window.title("Motivation Booster")
    window.geometry("500x500")

    # შეკითხვები და მათი გასაღებები
    entries = {}
    questions = [
        ("work_satisfaction", "სამუშაოს კმაყოფილება (0-1)"),
        ("goal_clarity", "მიზნის სიცხადე (0-1)"),
        ("recent_progress", "ბოლო პროგრესი (0-1)"),
        ("stress_level", "სტრესის დონე (0-1)"),
        ("time_management", "დროის მართვის უნარი (0-1)")
    ]

    # შექმნის ყველა შეკითხვას და მათ შესაბამის Entry ველებს
    for key, question in questions:
        label = tk.Label(window, text=question, font=("Helvetica", 12))
        label.pack(pady=5)
        entry = tk.Entry(window)
        entry.pack(pady=5)
        entries[key] = entry  # შემოაქვს Entry ველი დიქტიონარში

    # ფუნქცია, რომელიც გამოხატავს შეკითხვების შედეგებს და ნეირონულ ქსელს
    def submit_answers():
        # მომხმარებლის მონაცემების შეგროვება
        user_data = {
            "work_satisfaction": float(entries["work_satisfaction"].get()),
            "goal_clarity": float(entries["goal_clarity"].get()),
            "recent_progress": float(entries["recent_progress"].get()),
            "stress_level": float(entries["stress_level"].get()),
            "time_management": float(entries["time_management"].get())
        }

        # მონაცემების გადამუშავება
        input_data = preprocess_data(user_data)

        # ნეირონული ქსელის აგება და ტრენინგი
        model = build_model()
        model = train_model(model)

        # პროგნოზის მიღება და რეკომენდაციების გენერაცია
        prediction = model.predict(input_data)[0][0]
        recommendations = recommend_improvements(prediction)

        # შედეგების გამოტანა GUI-ზე
        result_text = "\nთქვენი რეკომენდაციები:\n"
        for rec in recommendations:
            result_text += f"- {rec}\n"

        result_label.config(text=result_text)  # ტექსტი შედეგის ლეიბლში

        # მონაცემების და რეკომენდაციების შენახვა JSON ფაილში
        save_results(user_data, recommendations)

    # ღილაკი, რომელიც დააჭერს submit_answers ფუნქციას
    submit_button = tk.Button(window, text="დაწყება", command=submit_answers)
    submit_button.pack(pady=20)

    # ლეიბლი, სადაც გამოჩნდება შედეგები
    result_label = tk.Label(window, text="", font=("Helvetica", 12))
    result_label.pack(pady=10)

    # ფანჯრის გაშვება
    window.mainloop()

# შემდგომი პროცესი
if __name__ == "__main__":
    start_gui()
