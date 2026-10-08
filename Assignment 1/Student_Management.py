#Student performance management system
students={
    101:{"Name":"Manasvi", "Scores": [90,88,95]},
    102:{"Name":"Swara", "Scores": [78,88,90]},
    103:{"Name":"Aarya", "Scores": [43,50,27]},
    104:{"Name":"Aum", "Scores": [86,89,81]},
    105:{"Name":"Rajas", "Scores": [59,72,69]}
}
print("Students with their scores are : ",students.items())
#Calculate avg score and flag pass or fail
for sid, details in students.items():
    avg=sum(details["Scores"])/len(details["Scores"])
    details["Average"]=avg
    details["Passed"]=avg >=50 #Boolean flag

#Print the names of students who passed
print()
print("Students who passed: ")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])
