import pandas as pd
import matplotlib.pyplot as plt

data = {
    "attendance_percent": [92, 67, 81, 45, 74, 88],
    "assignment_score": [18, 12, 15, 8, 14, 19],
    "quiz_score": [72, 48, 65, 30, 55, 80]
}

df = pd.DataFrame(data)

df["total_score"] = df["assignment_score"] + df["quiz_score"]

plt.figure(figsize=(8, 5))
plt.scatter(df["attendance_percent"], df["total_score"])
plt.title("Attendance vs Total Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Total Score")
plt.show()
