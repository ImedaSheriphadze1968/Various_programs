from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import numpy as np

def build_model():
    """
    აგებს მარტივ ნეირონულ ქსელს.
    """
    model = Sequential([
        Input(shape=(5,)),  # 5 შემავალი ნეირონი მომხმარებლის მონაცემებისთვის
        Dense(10, activation='relu'),
        Dense(10, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(model):
    """
    ტრენინგისთვის იყენებს ფიქტიურ მონაცემებს. შეცვალეთ რეალური მონაცემებისთვის.
    """
    # ფიქტიური მონაცემები
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(0, 2, 100)

    model.fit(X_train, y_train, epochs=500, batch_size=10, verbose=1)
    return model
