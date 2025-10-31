# Edulytics

### Transforming academic data into meaningful insights

---

## Overview

**Edulytics+** is a smart Python-based program designed to turn raw student performance data into actionable academic insights.  
Built as part of an introductory programming project, it blends **data analysis, psychology, and performance visualization** to explore what truly affects learning outcomes.

The system analyzes **grades, attendance, study hours, sleep patterns, and stress levels**, uncovering relationships that influence academic success.  
It empowers both **students and educators** to move beyond “what” the results are — and start understanding “why” they occur.

---

## Key Features

| Feature | Description |
|----------|-------------|
| **Data Analysis Engine** | Reads and processes CSV-based student performance datasets using `pandas`. |
| **Object-Oriented Design** | Each student record is represented as a class instance with dynamic metrics like `Wellness_Index`. |
| **Correlation Insights** | Uses `numpy` and `seaborn` to uncover meaningful relationships between academic and lifestyle factors. |
| **Stress & Study Impact** | Quantifies how study hours and stress levels influence total scores. |
| **Wellness Modelling** | Calculates a personalized “Wellness Index” combining study, sleep, and stress. |
| **Comparative Analytics** | Contrasts top vs bottom performers to identify habits driving academic excellence. |
| **Predictive Forecasting** | Estimates score improvement potential based on behavioral adjustments. |
| **Report Generation** | Saves session summaries to text files for later review or academic reflection. |

---
## Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Programming Language** | Python 3.10+ |
| **Libraries** | `pandas`, `numpy`, `matplotlib`, `seaborn`, `colorama`, `time`, `os` |
| **Concepts** | Object-Oriented Programming (OOP), File Handling, Data Visualization, Correlation Analysis |

---

## System Architecture

The project follows a modular, class-based design:
```
Edulytics
│
├── Student class → represents each student and computes their wellness score.
│
├── Edulytics class → main analysis engine.
│   ├── correlation_insights() – explores variable relationships
│   ├── stress_performance() – examines stress vs performance
│   ├── study_effect() – analyzes study hour impact
│   ├── top_vs_bottom() – compares habits of high vs low performers
│   ├── personal_insight() – provides student-specific feedback
│   ├── lifestyle_report() – evaluates class-wide lifestyle quality
│   ├── forecast() – projects academic growth potential
│   └── export_summary() – generates a text-based insight file
│
└── Main Dashboard – interactive menu that lets users choose analyses.
```

---

## Sample Analyses

### 1. **Correlation Heatmap**
Visualizes how academic and lifestyle variables interact (e.g., study hours, stress, wellness).

### 2. **Stress vs Performance**
Quantifies whether stress correlates positively or negatively with total scores.

### 3. **Top vs Bottom Comparison**
Highlights behavioral differences (study time, sleep, stress) between top and struggling students.

### 4. **Forecast Simulation**
Predicts potential score improvement if students increase study hours or reduce stress.

### 5. **Personalized Insights**
Provides individual-level feedback on wellness and academic balance.

---

## Project Structure

```
Edulytics/
│
├── Students Performance Dataset.csv
│
├── edulytics.py
│
├── session_insights_<timestamp>.txt
│
└── README.md
```

---

## Example Dataset Columns

| Column | Description |
|---------|-------------|
| Student_ID | Unique identifier for each student |
| First_Name / Last_Name | Student details |
| Department | Field of study (Maths, CS, Engineering, etc.) |
| Attendance (%) | Course attendance rate |
| Midterm_Score / Final_Score | Exam performance |
| Assignments_Avg / Quizzes_Avg | Continuous assessment metrics |
| Study_Hours_per_Week | Average weekly study hours |
| Sleep_Hours_per_Night | Average sleep hours |
| Stress_Level (1–10) | Self-reported stress score |
| Extracurricular_Activities | Yes/No |
| Total_Score | Overall performance index |

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/mridulkhanna2/Edulytics.git
```

### 2. Navigate to the project folder
```bash
cd Edulytics
```

### 3. Run the program
```bash
python edulytics.py
```

---

## Future Enhancements
- Integrate **machine learning models** for performance prediction  
- Add **Plotly/Dash dashboards** for interactive visualization  
- Enable **teacher vs student view modes**  
- Include **real-time data import** from learning management systems
- Add relevant analytics

---


## Dataset Reference

This project uses the **Students Grading Dataset** available on Kaggle, created by Mahmoud El Hemaly.  
It provides anonymized academic and lifestyle data for students, including scores, attendance, study habits, and stress levels — ideal for analyzing performance and wellness correlations.  

🔗 [Kaggle Dataset – Students Grading Dataset](https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset)

---

## Author
**Mridul Khanna**  
540875559
Master’s in Computer Science
University of Sydney  

---

## Acknowledgments
- Project developed as part of *Intro to Programming* coursework  
- Dataset adapted for educational use and testing  
- Special thanks to mentors and peers for feedback and collaboration  
---

### 🌟 Built to make learning measurable, meaningful, and mindful.
