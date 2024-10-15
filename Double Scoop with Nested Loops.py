# Task 1. Your Mood Tracker

import random

moods = ["happy", "sad", "tired"]
times_of_day = ["morning", "afternoon", "evening"]
days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


for day in days_of_week:
    time = random.choice(times_of_day)
    mood = random.choice(moods)

    print(f"On {day} {time} you were {mood}.")
    





