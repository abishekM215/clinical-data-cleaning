import pandas as pd

# Step 1: Load sample clinical trial data
data = {
    "Patient_ID": [1, 2, 3, 4],
    "Age": [34, None, 45, -5],
    "Visit_Date": ["2023-01-10", "2023-01-05", "2023-02-01", "2022-12-30"],
    "Enrollment_Date": ["2023-01-01", "2023-01-10", "2023-01-15", "2023-01-05"]
}

df = pd.DataFrame(data)

# Step 2: Convert dates
df["Visit_Date"] = pd.to_datetime(df["Visit_Date"])
df["Enrollment_Date"] = pd.to_datetime(df["Enrollment_Date"])

# Step 3: Data validation checks
df["Age_Issue"] = df["Age"].isnull() | (df["Age"] <= 0)
df["Date_Issue"] = df["Visit_Date"] < df["Enrollment_Date"]

# Step 4: Show problem records
issues = df[df["Age_Issue"] | df["Date_Issue"]]
print("Records with issues:")
print(issues)

# Step 5: Simple cleaning
df.loc[df["Age_Issue"], "Age"] = df["Age"].median()

print("\nCleaned Data:")
print(df)

