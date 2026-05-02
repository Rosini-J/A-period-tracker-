from datetime import datetime, timedelta

def save_entry(date, cycle_day, pain_level,
               mood, mood_rate, food, journal):
    with open("period_log.txt", "a") as file:
        file.write("\n----- New Entry -----\n")
        file.write(f"Date: {date}\n")
        file.write(f"Cycle Day: {cycle_day}\n")
        file.write(f"Pain Level: {pain_level}/10\n")
        file.write(f"Mood: {mood} ({mood_rate})\n")
        file.write(f"Cravings: {food}\n")
        file.write(f"Thoughts: {journal}\n")

def add_entry():
    print("\n🌸 ----- Your Wellness Journal ----- 🌸\n")
    date = input("What's today's date (dd-mm-yyyy): ")
    cycle_day = int(input("\nCycle day (eg. 1, 2..): "))
    pain_level = int(input("\nRate the cramps out of 10: "))

    if pain_level > 6:
        print("\n ~> It's okay to rest today."
              " A warm heating pad might help 🌿")

    mood = input("\nHow's your mood today (okay, anxious,"
                 " anger, lonely, irritable): ").lower()
    mood_rate = input("\nRate your mood (low, moderate, high): ")
    food = input("\nAny cravings in mind: ")

    if "anxious" in mood or "lonely" in mood:
        print(f"\n ~> It's okay to feel this way."
              f" Be gentle with yourself today 🌸"
              f"\n ~> Maybe some {food} and soft music"
              f" will bring a little comfort 🎵")
    elif "anger" in mood or "irritable" in mood:
        print(f"\n ~> Your feelings are valid 💙"
              f" It's okay to feel irritable today."
              f"\n ~> Take it slow, maybe treat yourself"
              f" to some {food} and a cozy show 🌙")
    else:
        print("\n ~> You're doing wonderfully 🌷"
              "\n ~> Keep taking care of yourself,"
              " one day at a time 💛")

    journal = input("\nThoughts for the day: ")

    save_entry(date, cycle_day, pain_level,
               mood, mood_rate, food, journal)

    print("\n ~> Your entry has been saved 🌸"
          "\n ~> Thank you for checking in"
          " with yourself today 💛")

    if cycle_day == 1:
        date_obj = datetime.strptime(date, "%d-%m-%Y")
        next_period = date_obj + timedelta(days=28)
        print(f"\n ~> Your next cycle is expected"
              f" around {next_period.strftime('%d-%m-%Y')} 🌙"
              f"\n ~> Take good care of yourself"
              f" until then 🌿")

def view_entries():
    try:
        with open("period_log.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("\n ~> No entries yet 🌸"
                      "\n ~> Start by adding today's entry —"
                      "\n ~> every small step of"
                      " self care matters 💛")
            else:
                print("\n🌸 ----- Your Wellness Log ----- 🌸")
                print(content)
    except FileNotFoundError:
        print("\n ~> No entries yet 🌸"
              "\n ~> Start by adding today's entry —"
              "\n ~> every small step of"
              " self care matters 💛")

def main():
    while True:
        print("\n🌸 ----- Your Wellness Journal ----- 🌸")
        print("\n1. Add today's entry")
        print("2. View past entries")
        print("3. Exit")

        choice = input("\nChoose (1/2/3): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("\n ~> Take care of yourself 🌸"
                  "\n ~> Remember — you are doing better"
                  " than you think 💛")
            break
        else:
            print("\n ~> Please choose 1, 2 or 3 🌸")

main()
