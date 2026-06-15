import pandas as pd
import matplotlib.pyplot as plt

data = {
    "lab_completed": [True, False, True, False, True, True]
}

df = pd.DataFrame(data)

counts = df["lab_completed"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    counts,
    labels=["Completed", "Not Completed"],
    autopct="%1.1f%%"
)
plt.title("Lab Completion Status")
plt.show()