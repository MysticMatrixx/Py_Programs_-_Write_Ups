
import pandas as p

nameOfStudentsWithMarks = {
     "Shibin"  : 50,
     "Shreenadh" : 60,
     "Manoj" : 70,
     "Chinna" : 80,
     "Siddanth" : 90,
}

s1 = p.Series(nameOfStudentsWithMarks)
s2 = p.Series(nameOfStudentsWithMarks)
s3 = p.Series(nameOfStudentsWithMarks)
s4 = p.Series(nameOfStudentsWithMarks)
s5 = p.Series(nameOfStudentsWithMarks)

df = p.DataFrame([s1,s2,s3,s4], index=["Math", "Bio", "Chem", "Phy"])

# df.loc["Eng"] = ["30","50","60","60","60"] # ACCESS ROW
# df["Jash"] = ["30","50","60","60","60"] # ACCESS COLUMN

# df.loc["Eng"] = ["0","0"] ERROR FOR BOTH COLUMN AND ROW
# df = df.drop("Eng", axis=0) # ROW=0 COLUMN=1

print(df)
