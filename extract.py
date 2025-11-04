print("Extract Data")

import pandas as pd

data = {
    "Name": ["Swapnil", "Akash", "Sumit", "Rahul", "Rohan"],
    "Age": [25, 28, 23, 24, 24],
    "Courses": ["Data Engineering", "Python", "Data Science", "SQL", "Linux"]
}

df = pd.DataFrame(data)

print(df)