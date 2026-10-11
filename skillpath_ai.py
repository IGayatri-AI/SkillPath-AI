import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

# SkillPath AI
# SDG 4: Quality Education
# A beginner-friendly personalized learning roadmap prototype


ROADMAPS = {
    "AI / Machine Learning": {
        "Beginner": [
            "Week 1: Learn Python basics and variables.",
            "Week 2: Practice conditions, loops and functions.",
            "Week 3: Learn lists, dictionaries and file handling.",
            "Week 4: Study basic mathematics for machine learning.",
            "Week 5: Learn NumPy and Pandas fundamentals.",
            "Week 6: Understand machine learning concepts.",
            "Week 7: Build a beginner data analysis project.",
            "Week 8: Create and document a simple ML project."
        ],
        "Intermediate": [
            "Week 1: Revise Python and data structures.",
            "Week 2: Practice NumPy and Pandas.",
            "Week 3: Learn data cleaning and visualization.",
            "Week 4: Study supervised learning algorithms.",
            "Week 5: Learn model training and evaluation.",
            "Week 6: Explore scikit-learn.",
            "Week 7: Build a machine learning project.",
            "Week 8: Document the project and publish it on GitHub."
        ],
        "resources": [
            "Python: https://www.w3schools.com/python/",
            "Machine Learning: https://developers.google.com/machine-learning/crash-course",
            "Practice: https://www.kaggle.com/learn",
            "Projects: https://github.com/"
        ]
    },

    "Web Development": {
        "Beginner": [
            "Week 1: Learn HTML basics.",
            "Week 2: Practice CSS and page layouts.",
            "Week 3: Learn JavaScript fundamentals.",
            "Week 4: Build a personal portfolio webpage.",
            "Week 5: Learn DOM manipulation.",
            "Week 6: Create an interactive website.",
            "Week 7: Learn responsive web design.",
            "Week 8: Publish your project online."
        ],
        "Intermediate": [
            "Week 1: Revise HTML, CSS and JavaScript.",
            "Week 2: Learn modern JavaScript features.",
            "Week 3: Explore a frontend framework.",
            "Week 4: Build reusable interface components.",
            "Week 5: Learn APIs and JSON.",
            "Week 6: Create a project using an API.",
            "Week 7: Learn backend development basics.",
            "Week 8: Publish a complete portfolio project."
        ],
        "resources": [
            "HTML, CSS and JavaScript: https://www.freecodecamp.org/",
            "Web tutorials: https://www.w3schools.com/",
            "Practice projects: https://github.com/"
        ]
    },

    "Data Science": {
        "Beginner": [
            "Week 1: Learn Python fundamentals.",
            "Week 2: Practice lists, dictionaries and functions.",
            "Week 3: Learn basic statistics.",
            "Week 4: Explore NumPy.",
            "Week 5: Learn Pandas for data analysis.",
            "Week 6: Create charts using Matplotlib.",
            "Week 7: Analyze a small dataset.",
            "Week 8: Present your findings in a project."
        ],
        "Intermediate": [
            "Week 1: Revise Python and statistics.",
            "Week 2: Practice data cleaning with Pandas.",
            "Week 3: Explore data visualization.",
            "Week 4: Study probability and distributions.",
            "Week 5: Perform exploratory data analysis.",
            "Week 6: Learn basic predictive modeling.",
            "Week 7: Build a data analysis project.",
            "Week 8: Publish your project and findings."
        ],
        "resources": [
            "Python: https://www.w3schools.com/python/",
            "Data Science: https://www.kaggle.com/learn",
            "Statistics: https://www.khanacademy.org/"
        ]
    },

    "Cybersecurity": {
        "Beginner": [
            "Week 1: Learn computer and operating system basics.",
            "Week 2: Understand networking fundamentals.",
            "Week 3: Study IP addresses, DNS and HTTP.",
            "Week 4: Learn Linux fundamentals.",
            "Week 5: Understand common security concepts.",
            "Week 6: Study passwords and authentication.",
            "Week 7: Practice in legal learning labs.",
            "Week 8: Document a cybersecurity awareness project."
        ],
        "Intermediate": [
            "Week 1: Revise networking fundamentals.",
            "Week 2: Practice Linux commands.",
            "Week 3: Study web security fundamentals.",
            "Week 4: Learn secure coding principles.",
            "Week 5: Explore authentication and access control.",
            "Week 6: Practice in authorized security labs.",
            "Week 7: Complete a defensive security project.",
            "Week 8: Document your learning and results."
        ],
        "resources": [
            "Networking: https://www.netacad.com/",
            "Cybersecurity learning: https://portswigger.net/web-security",
            "Security education: https://tryhackme.com/"
        ]
    },

    "Software Development": {
        "Beginner": [
            "Week 1: Learn Python fundamentals.",
            "Week 2: Practice conditions and loops.",
            "Week 3: Learn functions and modules.",
            "Week 4: Study lists, dictionaries and strings.",
            "Week 5: Understand object-oriented programming.",
            "Week 6: Practice problem-solving exercises.",
            "Week 7: Build a small desktop application.",
            "Week 8: Upload your project to GitHub."
        ],
        "Intermediate": [
            "Week 1: Revise programming fundamentals.",
            "Week 2: Practice data structures.",
            "Week 3: Study algorithms and complexity.",
            "Week 4: Learn object-oriented design.",
            "Week 5: Practice debugging and testing.",
            "Week 6: Learn Git and GitHub.",
            "Week 7: Build a complete application.",
            "Week 8: Test, document and publish the project."
        ],
        "resources": [
            "Python: https://www.w3schools.com/python/",
            "Programming practice: https://www.hackerrank.com/",
            "Version control: https://docs.github.com/"
        ]
    }
}


class SkillPathAI:
    def __init__(self, root):
        self.root = root
        self.root.title("SkillPath AI | Quality Education")
        self.root.geometry("850x720")
        self.root.minsize(700, 600)

        self.root.configure(bg="#f0f4f8")

        self.create_interface()

    def create_interface(self):
        # Header
        header = tk.Frame(self.root, bg="#173b65", pady=18)
        header.pack(fill="x")

        tk.Label(
            header,
            text="SkillPath AI",
            font=("Arial", 25, "bold"),
            fg="white",
            bg="#173b65"
        ).pack()

        tk.Label(
            header,
            text="Personalized Learning & Career Guidance",
            font=("Arial", 11),
            fg="#dbeafe",
            bg="#173b65"
        ).pack(pady=4)

        # SDG information
        tk.Label(
            self.root,
            text="SDG 4: QUALITY EDUCATION",
            font=("Arial", 10, "bold"),
            fg="#166534",
            bg="#dcfce7",
            pady=8
        ).pack(fill="x", padx=20, pady=12)

        # Input area
        form = tk.Frame(self.root, bg="#f0f4f8")
        form.pack(fill="x", padx=30, pady=5)

        tk.Label(
            form, text="Your Name:",
            font=("Arial", 11, "bold"),
            bg="#f0f4f8"
        ).grid(row=0, column=0, sticky="w", pady=8)

        self.name_entry = tk.Entry(form, font=("Arial", 11), width=28)
        self.name_entry.grid(row=0, column=1, padx=12, sticky="w")

        tk.Label(
            form, text="Career Goal:",
            font=("Arial", 11, "bold"),
            bg="#f0f4f8"
        ).grid(row=1, column=0, sticky="w", pady=8)

        self.career = ttk.Combobox(
            form,
            values=list(ROADMAPS.keys()),
            state="readonly",
            width=27,
            font=("Arial", 10)
        )
        self.career.grid(row=1, column=1, padx=12, sticky="w")
        self.career.set("AI / Machine Learning")

        tk.Label(
            form, text="Current Skill Level:",
            font=("Arial", 11, "bold"),
            bg="#f0f4f8"
        ).grid(row=2, column=0, sticky="w", pady=8)

        self.level = ttk.Combobox(
            form,
            values=["Beginner", "Intermediate"],
            state="readonly",
            width=27,
            font=("Arial", 10)
        )
        self.level.grid(row=2, column=1, padx=12, sticky="w")
        self.level.set("Beginner")

        tk.Label(
            form, text="Study Hours per Day:",
            font=("Arial", 11, "bold"),
            bg="#f0f4f8"
        ).grid(row=3, column=0, sticky="w", pady=8)

        self.hours = ttk.Combobox(
            form,
            values=["1 hour", "2 hours", "3 hours", "4+ hours"],
            state="readonly",
            width=27,
            font=("Arial", 10)
        )
        self.hours.grid(row=3, column=1, padx=12, sticky="w")
        self.hours.set("2 hours")

        # Buttons
        buttons = tk.Frame(self.root, bg="#f0f4f8")
        buttons.pack(pady=12)

        tk.Button(
            buttons,
            text="Generate My Learning Path",
            command=self.generate_plan,
            bg="#1769aa",
            fg="white",
            activebackground="#12538a",
            font=("Arial", 11, "bold"),
            padx=12,
            pady=9,
            cursor="hand2"
        ).pack(side="left", padx=5)

        tk.Button(
            buttons,
            text="Save My Plan",
            command=self.save_plan,
            bg="#16803c",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=12,
            pady=9,
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Output area
        tk.Label(
            self.root,
            text="Your Personalized Learning Roadmap",
            font=("Arial", 13, "bold"),
            bg="#f0f4f8",
            fg="#173b65"
        ).pack(anchor="w", padx=25, pady=(8, 4))

        self.output = ScrolledText(
            self.root,
            height=16,
            font=("Arial", 10),
            wrap="word",
            bg="white",
            padx=12,
            pady=10
        )
        self.output.pack(fill="both", expand=True, padx=25, pady=(0, 18))

        self.output.insert(
            "1.0",
            "Welcome to SkillPath AI!\n\n"
            "Select your career goal and skill level, then click "
            "'Generate My Learning Path' to receive your roadmap.\n\n"
            "Your goal: Learn step by step, build projects, and develop "
            "career-ready skills."
        )
        self.output.config(state="disabled")

    def generate_plan(self):
        name = self.name_entry.get().strip()
        career = self.career.get()
        level = self.level.get()
        hours = self.hours.get()

        if not career or not level or not hours:
            messagebox.showwarning(
                "Missing Information",
                "Please select your career goal, skill level and study hours."
            )
            return

        if not name:
            name = "Learner"

        selected = ROADMAPS[career]
        weekly_plan = selected[level]
        resources = selected["resources"]

        result = (
            "SKILLPATH AI - PERSONALIZED LEARNING PLAN\n"
            + "=" * 48 + "\n\n"
            + "Welcome, " + name + "!\n\n"
            + "Career Goal: " + career + "\n"
            + "Current Level: " + level + "\n"
            + "Daily Study Time: " + hours + "\n"
            + "Roadmap Duration: 8 Weeks\n\n"
            + "YOUR WEEK-BY-WEEK ROADMAP\n"
            + "-" * 35 + "\n\n"
        )

        for week in weekly_plan:
            result += "• " + week + "\n"

        result += (
            "\nRECOMMENDED LEARNING RESOURCES\n"
            + "-" * 35 + "\n\n"
        )

        for resource in resources:
            result += "• " + resource + "\n"

        result += (
            "\nYOUR ACTION PLAN\n"
            + "-" * 35 + "\n\n"
            + "1. Follow the roadmap at your own pace.\n"
            + "2. Practice regularly according to your schedule.\n"
            + "3. Build small projects to apply your knowledge.\n"
            + "4. Document your work on GitHub when appropriate.\n"
            + "5. Review your progress every week.\n\n"
            + "PROJECT ALIGNMENT\n"
            + "-" * 35 + "\n\n"
            + "SkillPath AI supports SDG 4: Quality Education by "
            + "organizing learning resources and providing "
            + "personalized, beginner-friendly learning guidance.\n\n"
            + "Note: This prototype uses predefined learning rules. "
            + "It does not yet use a trained AI model or live "
            + "recommendation engine."
        )

        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", result)
        self.output.config(state="disabled")

    def save_plan(self):
        content = self.output.get("1.0", tk.END).strip()

        if not content or "Welcome to SkillPath AI!" in content:
            messagebox.showinfo(
                "No Plan Yet",
                "Generate your learning plan before saving."
            )
            return

        path = filedialog.asksaveasfilename(
            title="Save Your SkillPath AI Plan",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            initialfile="SkillPath_AI_Learning_Plan.txt"
        )

        if path:
            try:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)

                messagebox.showinfo(
                    "Success",
                    "Your learning plan has been saved successfully!"
                )
            except OSError as error:
                messagebox.showerror(
                    "Save Error",
                    "Could not save the file:\n" + str(error)
                )


if __name__ == "__main__":
    window = tk.Tk()
    app = SkillPathAI(window)
    window.mainloop()
