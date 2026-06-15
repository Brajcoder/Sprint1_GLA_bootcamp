import pandas as pd
import matplotlib.pyplot as plt

data = {
    "student_id": [101, 102, 103, 104, 105, 106],
    "attendance_percent": [92, 67, 81, 45, 74, 88]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.bar(df["student_id"], df["attendance_percent"])
plt.title("Attendance Percentage by Student")
plt.xlabel("Student ID")
plt.ylabel("Attendance (%)")
plt.show()

data = {
    "student_id": [101, 102, 103, 104, 105, 106],
    "attendance_percent": [92, 67, 81, 45, 74, 88]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.bar(df["student_id"], df["attendance_percent"])
plt.title("Attendance Percentage by Student")
plt.xlabel("Student ID")
plt.ylabel("Attendance (%)")
plt.show()