
from datetime import datetime

name = input("Enter your name: ")
mood = input("How are you feeling today? (happy, sad, stressed, tired, excited): ").lower()
energy = int(input("Enter your energy level from 1 to 10: "))

print("\n==============================")
print("MY DAILY MOOD ADVISOR")
print("==============================")

print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy, "/10")

if energy <= 3:
    print("Your energy is very low. Take a break and get some rest.")

if energy >= 5:
    print("You have enough energy for today's activities.")
else:
    print("Try to take things slowly and save your energy.")

if mood == "happy":
    advice = "Keep smiling and share your positive energy!"
elif mood == "sad":
    advice = "Take some time for yourself and talk to someone you trust."
elif mood == "stressed":
    advice = "Take a few deep breaths and work on one task at a time."
elif mood == "tired":
    advice = "Relax for a while and make sure you get enough sleep."
elif mood == "excited":
    advice = "Use your excitement to work on something you enjoy!"
else:
    advice = "Stay positive and take care of yourself today."

print("Daily Advice:", advice)

current_time = datetime.now()

print("\n==============================")
print("DAILY MOOD REPORT")
print("==============================")
print("User:", name)
print("Today's Mood:", mood)
print("Energy Level:", energy)
print("Advice:", advice)
print("Date:", current_time.strftime("%d-%m-%Y"))
print("Time:", current_time.strftime("%I:%M %p"))
print("==============================")
