import pandas as pd
import matplotlib.pyplot as plt

data = {
    "attendance_percent": [92, 67, 81, 45, 74, 88],
    "assignment_score": [18, 12, 15, 8, 14, 19],
    "quiz_score": [72, 48, 65, 30, 55, 80],
    "lab_completed": [True, False, True, False, True, True]
}

df = pd.DataFrame(data)

df["total_score"] = df["assignment_score"] + df["quiz_score"]

df["eligible"] = (
    (df["attendance_percent"] >= 75) &
    (df["total_score"] >= 70) &
    (df["lab_completed"])
)

counts = df["eligible"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    counts,
    labels=["Eligible", "Not Eligible"],
    autopct="%1.1f%%"
)
plt.title("Eligibility Distribution")
plt.show()