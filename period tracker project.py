
from datetime import datetime, timedelta


# 1. Get menstrual cycle phase

def get_phase(cycle_day):

    if 1 <= cycle_day <= 5:
        return "menstrual"

    elif 6 <= cycle_day <= 13:
        return "follicular"

    elif 14 <= cycle_day <= 16:
        return "ovulation"

    elif 17 <= cycle_day <= 28:
        return "luteal"

    else:
        return None


# 2. Get current time of day

def get_time_of_day():

    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "morning"

    elif 12 <= hour < 17:
        return "afternoon"

    elif 17 <= hour < 21:
        return "evening"

    else:
        return "night"


# 3. Get journal prompt

def get_journal_prompt(phase, time_of_day):

    prompts = {

        "menstrual": {
            "morning": "How is your body feeling right now?",
            "afternoon": "What has your body been telling you today?",
            "evening": "What did you need most today?",
            "night": "What did your body ask for today? Did you listen?"
        },

        "follicular": {
            "morning": "What do you want to focus on today?",
            "afternoon": "What has felt easy or natural today?",
            "evening": "What did you accomplish today, big or small?",
            "night": "What went well today?"
        },

        "ovulation": {
            "morning": "What are you looking forward to today?",
            "afternoon": "What feels exciting or energising right now?",
            "evening": "What are you proud of today?",
            "night": "What connection or conversation meant something to you today?"
        },

        "luteal": {
            "morning": "What is one gentle thing you can do for yourself today?",
            "afternoon": "How are you holding up today?",
            "evening": "What emotion has been loudest today?",
            "night": "What do you want to let go of before sleeping?"
        }
    }

    return prompts[phase][time_of_day]


# 4. Get cycle day

def get_cycle_day():

    while True:

        try:

            cycle_day = int(input("Enter your current cycle day (1-28): "))

            if 1 <= cycle_day <= 28:
                return cycle_day

            else:
                print("Please enter a number between 1 and 28.")

        except ValueError:
            print("Please enter a valid number.")


# 5. Journal functions

def write_journal():

    print("\n<--JOURNAL-->")

    cycle_day = get_cycle_day()

    phase = get_phase(cycle_day)

    time_of_day = get_time_of_day()

    prompt = get_journal_prompt(phase, time_of_day)

    
    print(f"\n{prompt}")

    entry = input("\nWrite your thoughts: ")
    if not entry:
         print("Nothing saved.")
         return

    date = datetime.today().strftime("%d-%m-%Y")

    with open("journal_log.txt", "a") as file:

        file.write("\n----- Journal Entry -----\n")
        file.write(f"Date: {date}\n")
        file.write(f"Cycle Day: {cycle_day}\n")
        file.write(f"Phase: {phase}\n")
        file.write(f"Time: {time_of_day}\n")
        file.write(f"Prompt: {prompt}\n")
        file.write(f"Journal: {entry}\n")

    print("\nJournal entry saved.")


def view_journal():

    print("\n<--VIEW JOURNAL-->")

    try:

        with open("journal_log.txt", "r") as file:
            content = file.read()

        if not content.strip():
            print("No journal entries found.")
            return

        print(content)

    except FileNotFoundError:

        print("No journal entries yet.")


def journal_menu():

    while True:

        print("\n<--JOURNAL-->")

        print("1. Write a journal entry")
        print("2. View journal")
        print("3. Back to main menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            write_journal()

        elif choice == "2":

            view_journal()

        elif choice == "3":

            break

        else:

            print("Invalid choice. Please try again.")


# 6. Add today's period entry

def add_entry():

    print("\n<--ADD TODAY'S ENTRY-->")

    date = datetime.today().strftime("%d-%m-%Y")

    print(f"\nToday's date: {date}")

    cycle_day = get_cycle_day()

    phase = get_phase(cycle_day)

    print(f"\nCycle phase: {phase}")

    flow = input("Enter your flow level: ")

    with open("period_log.txt", "a") as file:

        file.write("\n----- New Entry -----\n")
        file.write(f"Date: {date}\n")
        file.write(f"Cycle Day: {cycle_day}\n")
        file.write(f"Phase: {phase}\n")
        file.write(f"Flow: {flow}\n")

    print("\nToday's entry has been saved.")


# 7. View past entries

def view_entries():

    print("\n<--PAST ENTRIES-->")

    try:

        with open("period_log.txt", "r") as file:
            content = file.read()

        if not content.strip():

            print("No entries found.")

            return

        print(content)

    except FileNotFoundError:

        print("No entries yet. Add an entry first.")


# 8. Predict next period

def predict_next():

    print("\n<--PREDICT NEXT PERIOD-->")

    try:

        with open("period_log.txt", "r") as file:
            content = file.read()

        entries = [

            entry.strip()

            for entry in content.split("----- New Entry -----")

            if entry.strip()

        ]

        if not entries:

            print("No entries found. Add an entry first.")

            return

        last_entry = entries[-1]

        last_date = None

        last_cycle_day = None

        for line in last_entry.split("\n"):

            if line.startswith("Date") and ":" in line:

                last_date = line.split(":", 1)[1].strip()

            elif line.startswith("Cycle Day") and ":" in line:

                try:

                    last_cycle_day = int(
                        line.split(":", 1)[1].strip()
                    )

                except ValueError:

                    print("Could not read the cycle day.")

                    return

        if not last_date or last_cycle_day is None:

            print("Could not read the last entry.")

            return

        last_date_obj = datetime.strptime(
            last_date,
            "%d-%m-%Y"
        )

        days_remaining = 28 - last_cycle_day

        next_period = last_date_obj + timedelta(
            days=days_remaining
        )

        print(f"\nLast entry date : {last_date}")
        print(f"Last cycle day  : Day {last_cycle_day}")

        print(
            f"Estimated next period: "
            f"{next_period.strftime('%d %B %Y')}"
        )

        print(
            "\nNote: This is only an estimate "
            "based on a 28-day cycle."
        )

    except FileNotFoundError:

        print("No entries yet. Add an entry first.")

    except ValueError:

        print("Error reading the date in your log file.")


# 9. Body insights

def get_body_insights(cycle_day):

    phase = get_phase(cycle_day)

    if phase == "menstrual":

        print("\nYour estimated phase: Menstrual")
        print("This is the beginning of the cycle.")
        print("Some people may experience bleeding, cramps,")
        print("tiredness, or lower energy.")

    elif phase == "follicular":

        print("\nYour estimated phase: Follicular")
        print("This phase occurs after menstruation.")
        print("Energy and mood may vary from person to person.")

    elif phase == "ovulation":

        print("\nYour estimated phase: Ovulation")
        print("Ovulation is when an egg may be released.")
        print("Cycle timing can vary between people.")

    elif phase == "luteal":

        print("\nYour estimated phase: Luteal")
        print("This phase occurs after ovulation.")
        print("Some people may notice PMS-related changes")
        print("such as mood changes, bloating, or breast tenderness.")


# 10. What is my body doing today?

def what_is_my_body_doing():

    print("\nWhat Is My Body Doing Today?")

    print("Reading your last entry...")

    try:

        with open("period_log.txt", "r") as file:
            content = file.read()

        entries = [

            entry.strip()

            for entry in content.split("----- New Entry -----")

            if entry.strip()

        ]

        if not entries:

            print("No entries found. Add an entry first.")

            return

        last_entry = entries[-1]

        last_date = None

        last_cycle_day = None

        for line in last_entry.split("\n"):

            if line.startswith("Date") and ":" in line:

                last_date = line.split(":", 1)[1].strip()

            elif line.startswith("Cycle Day") and ":" in line:

                try:

                    last_cycle_day = int(
                        line.split(":", 1)[1].strip()
                    )

                except ValueError:

                    print("Could not read the cycle day.")

                    return

        if not last_date or last_cycle_day is None:

            print("Could not read the last entry.")

            return

        last_date_obj = datetime.strptime(
            last_date,
            "%d-%m-%Y"
        )

        today = datetime.today()

        days_passed = (today - last_date_obj).days

        if days_passed < 0:

            print("The last entry date cannot be in the future.")

            return

        current_cycle_day = last_cycle_day + days_passed

        while current_cycle_day > 28:

            current_cycle_day -= 28

        print(f"\nLast logged : {last_date}")
        print(f"Days since  : {days_passed} day(s)")

        print(
            f"Estimated cycle day today: "
            f"Day {current_cycle_day}"
        )

        get_body_insights(current_cycle_day)

    except FileNotFoundError:

        print("No entries yet. Add your first entry.")

    except ValueError:

        print("Error reading the date in your log file.")


# 11. PCOS and PCOD information

def pcos_info():

    print("\nPCOS and PCOD Information")

    print("\nWhat is PCOS?")

    print(
        "PCOS (Polycystic Ovary Syndrome) is a common "
        "hormonal condition."
    )

    print(
        "It can affect menstrual periods, ovulation, "
        "and androgen hormone levels."
    )

    print(
        "Some people with PCOS may also experience "
        "metabolic changes."
    )

    print("\nPossible symptoms:")

    print("- Irregular periods")
    print("- Acne")
    print("- Increased facial or body hair")
    print("- Hair thinning")
    print("- Difficulty with ovulation")
    print("- Weight changes")

    print("\nWhat is PCOD?")

    print(
        "PCOD is a term that is sometimes used differently "
        "in different places."
    )

    print(
        "It is not always treated as a separate medical "
        "diagnosis from PCOS."
    )

    print(
        "\nIf you are concerned about symptoms or your "
        "menstrual cycle, speak with a qualified doctor."
    )

    print(
        "\nThis app provides general awareness only "
        "and cannot diagnose PCOS, PCOD, or any other "
        "medical condition."
    )


# 12. Main menu

def show_menu():

    print("\n <--PERIOD TRACKER-->\n")

    print("1. Add today's entry")
    print("2. View past entries")
    print("3. Predict next period")
    print("4. What is my body doing today?")
    print("5. Journal")
    print("6. PCOS and PCOD information")
    print("7. Exit")

    print("\nIf it's your first time using the app, choose 1.")


# 13. Main program

def main():

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            add_entry()

        elif choice == "2":

            view_entries()

        elif choice == "3":

            predict_next()

        elif choice == "4":

            what_is_my_body_doing()

        elif choice == "5":

            journal_menu()

        elif choice == "6":

            pcos_info()

        elif choice == "7":

            print("\nThank you for using the Period Tracker.")

            break

        else:

            print("\nInvalid choice. Please enter 1-7.")


main()


