import numpy as np

def preprocess_data(user_data):
    """
    გადაქცევს მომხმარებლის მონაცემებს ნეირონული ქსელის შესატყვის ფორმატში.
    """
    # მაგალითისთვის, ვივარაუდოთ, რომ მონაცემები სტანდარტიზებულია [0, 1] დიაპაზონში
    data = [
        user_data["work_satisfaction"],
        user_data["goal_clarity"],
        user_data["recent_progress"],
        user_data["stress_level"],
        user_data["time_management"]
    ]
    return np.array([data])  # მოამზადებს ფორმატს, რომ TensorFlow შეძლოს გამოყენება
