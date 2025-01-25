import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generate_graph(tasks, hours, distractions, bar_color="#4CAF50"):
    # შექმნათ ფიგურა და მასზე გრაფიკი
    fig, ax = plt.subplots(figsize=(6, 4))

    # დავალებების სახელები და მათი საათები
    ax.bar(tasks, hours, color=bar_color)

    # y-ღერძი – დრო
    ax.set_ylabel('Hours')

    # x-ღერძი – დავალებები
    ax.set_xlabel('Tasks')

    # გრაფიკის სათაური
    ax.set_title('Task Hours')

    return fig, ax
