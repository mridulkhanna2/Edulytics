"""
Edulytics

Note:
- Graphs would not open in Ed, as they open in a seperate window, would suggest to use an IDE like Visual Studio or similar. You can also refer the insights from Option 8 - summary report
- Please close graph windows after viewing them, then press Enter when prompted 
  to return to the dashboard.
- If the first function fails, please run:
      pip install -r requirements.txt
"""


# Auto-install dependencies if missing
import subprocess
import sys
import os

req_file = "requirements.txt"
if os.path.exists(req_file):
    try:
        # Install missing packages
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
    except Exception as e:
        print(" Could not auto-install some packages. Please run:   ")
        print("pip install -r requirements.txt")

import os
import pandas as pd
import numpy as np
from colorama import Fore, Style, init
import time
import random

# optional visualization setup
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set(style="whitegrid", palette="muted")
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


# Represents a single student record
class Student:
    def __init__(self, row):
        self.id = row["Student_ID"]
        self.name = f"{row['First_Name']} {row['Last_Name']}"
        self.study = float(row["Study_Hours_per_Week"])
        self.sleep = float(row["Sleep_Hours_per_Night"])
        self.stress = float(row["Stress_Level (1-10)"])
        self.total = float(row["Total_Score"])
        self.dept = row["Department"]
        self.extra = row["Extracurricular_Activities"].strip().lower() == "yes"

    def compute_wellness(self):
        # basic formula combining study, rest, and stress
        bonus = 5 if self.extra else 0
        return round((0.6 * self.sleep + 0.7 * self.study + bonus) - (1.2 * self.stress), 2)


# Main Edulytics app
class Edulytics:
    def __init__(self, file="Students Performance Dataset.csv"):
        if not os.path.exists(file):
            print("File not found:", file)
            exit()

        self.df = pd.read_csv(file)
        self.students = [Student(row) for _, row in self.df.iterrows()]
        self.df["Wellness_Index"] = [s.compute_wellness() for s in self.students]

        # create or clear the log file
        self.session_file = f"output_session_insights_{time.strftime('%H%M%S')}.txt"
        open(self.session_file, "w", encoding="utf-8").close()

        self.show_welcome()
        print(len(self.df), "student records loaded.\n")

    def show_welcome(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("WELCOME TO EDULYTICS - Academic Insight Engine\n ")
        print("Analyzing the story behind your grades...\n")
        time.sleep(1.2)

    def pause(self):
        input("\nPress Enter to return to the dashboard...")
        os.system("cls" if os.name == "nt" else "clear")

    def log(self, text):
        with open(self.session_file, "a", encoding="utf-8") as f:
            f.write(text + "\n")

    def loading(self, message="Analyzing"):
        for i in range(3):
            print(f"{message}{'.' * (i + 1)}", end="\r")
            time.sleep(0.4)
        print(" " * 20, end="\r")

    # 1. Correlation Insights
    def correlation_insights(self):
        print("\n[1] CORRELATION ANALYSIS\n" + "-" * 50)
        self.loading("Calculating relationships")

        df = self.df.select_dtypes(include=["number"])
        corr = df.corr().round(2)
        found = False

        for (a, b), c in corr.unstack().sort_values(ascending=False).items():
            if a != b and abs(c) > 0.5:
                print(f"Strong correlation: {a} ↔ {b} ({c})")
                self.log(f"Strong correlation: {a}-{b}: {c}")
                found = True
                break

        if not found:
            print("No strong correlations found (>0.5).")

        if MATPLOTLIB_AVAILABLE:
            plt.figure(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Heatmap: Academic & Lifestyle Factors")
            plt.tight_layout()
            plt.show()
            print("\n(Note: If the graph window does not open, please check your environment or IDE settings.)")


        self.pause()

    # 2. Stress vs Performance
    def stress_performance(self):
        print("\n[2] STRESS vs PERFORMANCE\n" + "-" * 50)
        self.loading("Analyzing stress impact")

        corr = self.df["Stress_Level (1-10)"].corr(self.df["Total_Score"]).round(2)
        print(f"Correlation: {corr}")

        if corr < -0.3:
            msg = "Higher stress tends to reduce performance."
        elif corr > 0.3:
            msg = "Mild stress may slightly improve focus."
        else:
            msg = "No strong relationship detected."
        print(msg)

        self.log(f"Stress vs Score correlation: {corr} → {msg}")
        self.pause()

    # 3. Study Hours Impact
    def study_effect(self):
        print("\n[3] STUDY HOURS IMPACT\n" + "-" * 50)
        self.loading("Comparing study habits")

        corr = self.df["Study_Hours_per_Week"].corr(self.df["Total_Score"]).round(2)
        print(f"Correlation: {corr}")

        msg = "Consistent study hours lead to improved scores. LETS BE DISCIPLINED!!!" if corr > 0.4 \
            else "Quality of study may matter more than quantity.!! QUALITY >>> QUANTITY"
        print(msg)

        if MATPLOTLIB_AVAILABLE:
            avg_by_study = self.df.groupby(pd.cut(self.df["Study_Hours_per_Week"], bins=5), observed=True)["Total_Score"].mean()

            avg_by_study.plot(kind="bar", color="teal", title="Average Total Score by Study Hour Group", rot=0)
            plt.tight_layout()
            plt.show()
            print("\n(Note: If the graph window does not open, please check your environment or IDE settings.)")

        self.log(f"Study Impact correlation: {corr} | {msg}")
        self.pause()

    # 4. Compare top and bottom performers
    def top_vs_bottom(self):
        print("\n[4] TOP vs BOTTOM PERFORMERS\n" + "-" * 50)
        self.loading("Comparing groups")

        top10 = self.df.nlargest(10, "Total_Score")
        bottom10 = self.df.nsmallest(10, "Total_Score")

        compare = pd.DataFrame({
            "Avg Study": [top10["Study_Hours_per_Week"].mean(), bottom10["Study_Hours_per_Week"].mean()],
            "Avg Sleep": [top10["Sleep_Hours_per_Night"].mean(), bottom10["Sleep_Hours_per_Night"].mean()],
            "Avg Stress": [top10["Stress_Level (1-10)"].mean(), bottom10["Stress_Level (1-10)"].mean()]
        }, index=["Top 10", "Bottom 10"]).round(2)

        print(compare)
        print("\n Observation: higher study and better rest usually mean higher performance.")
        self.log(str(compare))
        self.pause()

    # 5. Personalized Student Insight
    def personal_insight(self):
        name = input("Enter Student Name or ID: ").strip().lower()
        match = self.df[self.df["Student_ID"].astype(str).str.lower() == name] if name.startswith("s") else \
                self.df[self.df["First_Name"].str.lower().str.contains(name)]

        if match.empty:
            print("Student not found.")
            return

        s = match.iloc[0]
        print(f"\nInsight for {s['First_Name']} {s['Last_Name']}")
        wellness = round((0.6 * s["Sleep_Hours_per_Night"] +
                          0.7 * s["Study_Hours_per_Week"]) - (1.2 * s["Stress_Level (1-10)"]), 2)
        print(f"Dept: {s['Department']} | Total Score: {s['Total_Score']}")
        print(f"Study: {s['Study_Hours_per_Week']}h | Sleep: {s['Sleep_Hours_per_Night']}h | Stress: {s['Stress_Level (1-10)']}")
        print(f"Wellness Index: {wellness}")

        if wellness > 5:
            msg = "Balanced and thriving! Going great kid! :D"
        elif wellness > 0:
            msg = "You are doing okay, could use a bit more rest. Sleep on time and meditate to reduce stress!"
        else:
            msg = "High stress detected :( ,you need better balance and rest."
        print(msg)
        self.log(f"Personal insight for {s['First_Name']} – {msg}")
        self.pause()

    # 6. Lifestyle Report
    def lifestyle_report(self):
        print("\n[6] LIFESTYLE QUALITY REPORT\n" + "-" * 50)

        avg_sleep = self.df["Sleep_Hours_per_Night"].mean()
        avg_study = self.df["Study_Hours_per_Week"].mean()
        avg_stress = self.df["Stress_Level (1-10)"].mean()

        grade = "A" if avg_sleep > 7 and avg_stress < 5 else "B" if avg_sleep > 6 else "C"
        print(f"Sleep: {avg_sleep:.1f} | Study: {avg_study:.1f} | Stress: {avg_stress:.1f}")
        print("Cohort Wellness Grade:", grade)

        msg = {
            "A": "Excellent overall balance! Nothing to worry about!",
            "B": "Fair lifestyle choice but some fatigue risk.",
            "C": "High stress or low rest in many students."
        }[grade]

        print(msg)
        self.log(f"Lifestyle report grade {grade}: {msg}")
        self.pause()

    # 7. Predictive Forecast
    def forecast(self):
        print("\n[7] ACADEMIC FORECAST SIMULATOR\n" + "-" * 50)
        self.loading("Running simulation")

        corr = self.df["Study_Hours_per_Week"].corr(self.df["Total_Score"])
        avg = self.df["Total_Score"].mean()
        gain = round(avg * corr * 0.07, 2)
        print(f"If students study 2 more hours weekly, scores may rise by ~{gain:.2f} points.")
        print("Balanced focus and rest = improvement.")
        self.log(f"Forecast gain: {gain}")
        self.pause()

    # 8. Recursive Study Planner
    def study_planner(self):
        print("\n[8] STUDY PLANNER (Recursive)\n" + "-" * 50)
        try:
            target = int(input("Target % improvement (e.g., 20): "))
            current = float(input("Current study hours per week: "))
            stress = float(input("Current stress level (1–10): "))
        except ValueError:
            print("Invalid input. Numbers only.")
            return

        efficiency = max(0.3, 1 - (stress / 20))

        def plan(target_increase, hours):
            if target_increase <= 0:
                return hours
            adjustment = (target_increase / 10) * efficiency
            print(f"Target +{target_increase}% → Study {hours + adjustment:.2f} hrs/week (eff {efficiency:.2f})")
            return plan(target_increase - 5, hours + adjustment)

        print("\nPlanning... please wait...\n")
        final = plan(target, current)
        print(f"\nTo achieve +{target}%, aim for around {final:.2f} hrs/week.\n")

        # added log entry
        log_msg = f"Study Planner → Target: +{target}%, Current: {current}, Stress: {stress}, Recommended: {final:.2f} hrs/week"
        self.log(log_msg)

        self.pause()

    # 9. Motivation Tip
    def motivation_tip(self):
        tips = [
            "Small progress every day adds up to big results.",
            "Discipline beats motivation - stay consistent.",
            "Balance is key to productivity.",
            "Don't study harder, study smarter.",
            "Rest well; your mind needs it too."
        ]
        print("\n[9] MOTIVATION OF THE DAY\n" + "-" * 50)
        print(random.choice(tips))
        self.pause()

    # 10. Summary
    def export_summary(self):
        top = self.df.loc[self.df["Total_Score"].idxmax()]
        avg = self.df["Total_Score"].mean()
        summary = f"""
EDULYTICS INSIGHT SUMMARY
Average Score: {avg:.2f}
Top Student: {top['First_Name']} {top['Last_Name']}
INSIGHTS SAVED TO: {self.session_file}
"""
        print(summary)
        self.log(summary)
        self.pause()

    # Dashboard
    def dashboard(self):
        while True:
            print("\nEDULYTICS DASHBOARD\n\n")
            print("1. Correlation Insights")
            print("2. Stress vs Performance")
            print("3. Study Hour Impact")
            print("4. Top vs Bottom Comparison")
            print("5. Personalized Insight")
            print("6. Lifestyle Report")
            print("7. Predictive Forecast")
            print("8. Summary Report")
            print("9. Motivation Tip")
            print("10. Study Planner (Recursive)")
            print("0. Exit")

            choice = input("\nEnter your choice: ").strip()
            os.system("cls" if os.name == "nt" else "clear")

            options = {
                "1": self.correlation_insights,
                "2": self.stress_performance,
                "3": self.study_effect,
                "4": self.top_vs_bottom,
                "5": self.personal_insight,
                "6": self.lifestyle_report,
                "7": self.forecast,
                "8": self.export_summary,
                "9": self.motivation_tip,
                "10": self.study_planner
            }

            if choice == "0":
                print("\n Thanks for using Edulytics!")
                print("Built to make learning measurable, meaningful, and mindful. See you again! :) ")
                break
            elif choice in options:
                options[choice]()
            else:
                print("Invalid choice.")
                time.sleep(1)


if __name__ == "__main__":
    app = Edulytics()
    app.dashboard()