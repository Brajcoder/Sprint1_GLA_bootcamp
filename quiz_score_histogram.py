import pandas as pd
import matplotlib.pyplot as plt

data = {
    "quiz_score": [72, 48, 65, 30, 55, 80]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.hist(df["quiz_score"], bins=5)
plt.title("Quiz Score Distribution")
plt.xlabel("Quiz Score")
plt.ylabel("Frequency")
plt.show()