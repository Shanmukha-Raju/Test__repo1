import pandas as pd
data={"Name":["shanmukh","vyom","sravan","monish","swaroop","santhosh","venkat","prasanth","abhinav","sumanth"],"maths":[34,45,56,78,65,45,23,98,76,54],"physics":[78,87,65,56,43,23,19,90,76,54],"chemistry":[35,87,65,43,92,94,82,71,93,79],"python":[98,97,96,95,94,93,92,91,90,100],"css":[56,67,83,21,23,89,76,81,94,90],"english":[100,97,95,93,91,98,96,94,92,90]}
df=pd.DataFrame(data)
print(df)
print(type(df))
print("average in maths",df["maths"].mean())
print("average in physics",df["physics"].mean())
print("average in chemistry",df["chemistry"].mean())
print("average in python",df["python"].mean())
print("average in css",df["css"].mean())
print("average in english",df["english"].mean())
df["Average"] = df[["maths", "physics", "chemistry", "python", "css", "english"]].mean(axis=1)
print("\nDataframe with average marks per student:")
print(df)

subjects = ["maths", "physics", "chemistry", "python", "css", "english"]
print("\nHighest marks and the student who achieved them in each subject:")
for subject in subjects:
  max_mark = df[subject].max()
  student_with_max_mark = df.loc[df[subject] == max_mark, "Name"].iloc[0]
  print(f"Subject: {subject}, Highest Mark: {max_mark}, Achieved by: {student_with_max_mark}")
