courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}
print("\n Courses:",courses)

courses["Data Structures"].update({"Alice":90})
courses["Data Structures"].pop("Charlie")
print("\n Charlie is removed and Alice marks are increased to:",courses["Data Structures"]["Alice"])

courses.update({"Web Development":{"Grace":95,"Henry":85}})
print("\n New course added:",courses)

if "Bob" not in courses["Algorithms"]:
    courses["Algorithms"].update({"Bob":80})
    print("\n Bob is now enrolled in Algorithms with marks:",courses["Algorithms"]["Bob"]) 
else:
    print("\n Bob is enrolled in Algorithms")

courses.pop("Machine Learning") 
print("\n Machine Learning is removed from courses:",courses)

Average=sum(courses["Data Structures"].values())/len(courses["Data Structures"])
print("\n Average grades of students in Data Structures:",Average)