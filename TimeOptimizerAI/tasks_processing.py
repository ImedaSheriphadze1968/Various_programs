def process_tasks(tasks, distractions, available_hours):
    """
    ამ ფუნქციამ უნდა გამოთვალოს ოპტიმიზებული დრო
    :param tasks: დავალებების დრო
    :param distractions: გაფანტული დრო
    :param available_hours: ხელმისაწვდომი საათები
    :return: ოპტიმიზირებული დრო
    """
    optimized_time = [(task - distraction) * available_hours for task, distraction in zip(tasks, distractions)]
    categories = [f"Task {i+1}" for i in range(len(tasks))]
    return optimized_time, categories
