print("-----Period blog-----\n")
date = input("What's today's date (dd-mm-yyyy): ")
cycle_day = int(input("\nCycle day (eg. 1, 2..): "))
pain_level = int(input("\nRate the cramps out of 10: "))

if pain_level > 6:
    print("\n\n ~> Let's use a heating pad !!")
mood = input("\n\n How's your mood today (okay, anxious, anger, lonely, irritable): ").lower()
mood_rate = input("\nRate your mood (low, moderate, high): ")
food = input("\n\nAny cravings in mind: ")
if "anxious" in mood or "lonely" in mood:
    print(f"\n\n ~> Hey girly, you're in your cycle, be chill. Let's eat some {food} and play music")
elif "anger" in mood or "irritable" in mood:
    print(f"\n\n~> Hello angry bird, let's watch a series and chat with our bestie. Let's buy some {food}")
else:
    print("\n\n~> Doing good pretty, let's have some fun and watch a series")


journal = input("\nThoughts for the day: ")

data = {
    "Date": date,
    "Cycle Day": cycle_day,
    "Pain": pain_level,
    "Mood": mood,
    "Mood Rate": mood_rate,
    "Cravings": food,
    "Thoughts": journal
}



# Save to file ← NEW PART
with open("period_log.txt", "a") as file:
    file.write("\n----- New Entry -----\n")
    file.write(f"Date: {date}\n")
    file.write(f"Cycle Day: {cycle_day}\n")
    file.write(f"Pain Level: {pain_level}/10\n")
    file.write(f"Mood: {mood} ({mood_rate})\n")
    file.write(f"Cravings: {food}\n")
    file.write(f"Thoughts: {journal}\n")

print("\nEntry saved to period_log.txt! ")