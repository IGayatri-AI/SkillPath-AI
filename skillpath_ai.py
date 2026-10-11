# SkillPath AI - Personalized Learning and Career Guidance

def recommend_path(interest, level):
    learning_paths = {
        "Artificial Intelligence": {
            "skills": ["Python", "Mathematics", "Machine Learning"],
            "projects": ["Student Performance Predictor", "AI Chatbot"]
        },
        "Web Development": {
            "skills": ["HTML", "CSS", "JavaScript"],
            "projects": ["Personal Portfolio Website", "Student Dashboard"]
        },
        "Data Science": {
            "skills": ["Python", "Statistics", "Data Visualization"],
            "projects": ["Student Marks Analysis", "Data Visualization Dashboard"]
        },
        "Cybersecurity": {
            "skills": ["Networking", "Linux Basics", "Security Fundamentals"],
            "projects": ["Password Strength Checker", "Security Awareness Guide"]
        }
    }

    path = learning_paths.get(interest)

    if not path:
        print("Sorry, no learning path found.")
        return

    print("\n===== YOUR PERSONALIZED LEARNING PATH =====")
    print("Interest:", interest)
    print("Current Level:", level)

    print("\nRecommended Skills:")
    for skill in path["skills"]:
        print("-", skill)

    print("\nSuggested Projects:")
    for project in path["projects"]:
        print("-", project)

    print("\nNext Step: Learn one skill at a time and practice regularly.")


def main():
    print("=" * 45)
    print("WELCOME TO SKILLPATH AI")
    print("Personalized Learning & Career Guidance")
    print("=" * 45)

    name = input("\nEnter your name: ").strip()

    interests = [
        "Artificial Intelligence",
        "Web Development",
        "Data Science",
        "Cybersecurity"
    ]

    print("\nChoose your area of interest:")
    for number, interest in enumerate(interests, start=1):
        print(f"{number}. {interest}")

    choice = input("\nEnter your choice (1-4): ").strip()

    if not name:
        name = "Student"

    try:
        choice_number = int(choice)
        if not 1 <= choice_number <= len(interests):
            raise ValueError
    except ValueError:
        print("Please restart and enter a number from 1 to 4.")
        return

    print("\nChoose your current skill level:")
    print("1. Beginner")
    print("2. Intermediate")

    level_choice = input("Enter your choice (1-2): ").strip()

    if level_choice == "1":
        level = "Beginner"
    elif level_choice == "2":
        level = "Intermediate"
    else:
        print("Invalid level. Please restart and choose 1 or 2.")
        return

    print(f"\nHello, {name}!")
    recommend_path(interests[choice_number - 1], level)

    print("\nThank you for using SkillPath AI!")


if __name__ == "__main__":
    main()
