import random
import time

# List of exercises
exercises = [
    "Rower", 
    "Prone Row", 
    "Push up", 
    "V-up", 
    "Leg Tuck and Twist", 
    "Supine Bike", 
    "The Swimmer"
]

def virtual_workout():
    # Randomly choose an exercise
    exercise = random.choice(exercises)
    # Fixed rep count of 5
    reps = 5
    print(f"Time to get moving! Do {reps} reps of {exercise}. No excuses, champ!")

if __name__ == "__main__":
    while True:
        virtual_workout()
        # Wait at least 30 minutes (randomized: between 30 and 45 minutes)
        wait_time = 30 * 60 + random.randint(0, 15 * 60)
        minutes = wait_time // 60
        print(f"Rest up, you'll get another surprise workout in about {minutes} minutes.")
        time.sleep(wait_time)
