# Task 1: Your mood today.

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


for day in days_of_week:
    mood = random.choice(moods)
    print(f"On {day}, I feel {mood}.")





