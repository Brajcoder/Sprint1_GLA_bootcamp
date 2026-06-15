import pandas as pd

data = {
    "student_id": [101, 102, 103, 104, 105, 106],
    "attendance_percent": [92, 67, 81, 45, 74, 88],
    "assignment_score": [18, 12, 15, 8, 14, 19],
    "quiz_score": [72, 48, 65, 30, 55, 80]
}

df = pd.DataFrame(data)

df["total_score"] = df["assignment_score"] + df["quiz_score"]

df["grade"] = pd.cut(
    df["total_score"],
    bins=[0, 50, 70, 85, 100],
    labels=["D", "C", "B", "A"]
)

df["attendance_category"] = pd.cut(
    df["attendance_percent"],
    bins=[0, 60, 80, 100],
    labels=["Low", "Medium", "High"]
)

df["risk_student"] = (
    (df["attendance_percent"] < 60) |
    (df["total_score"] < 50)
)

print(df)