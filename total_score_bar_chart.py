import pandas as pd
import matplotlib.pyplot as plt

data = {
    "student_id": [101, 102, 103, 104, 105, 106],
    "assignment_score": [18, 12, 15, 8, 14, 19],
    "quiz_score": [72, 48, 65, 30, 55, 80]
}

df = pd.DataFrame(data)

df["total_score"] = df["assignment_score"] + df["quiz_score"]

plt.figure(figsize=(8, 5))
plt.bar(df["student_id"], df["total_score"])
plt.title("Total Score by Student")
plt.xlabel("Student ID")
plt.ylabel("Total Score")
plt.show()