last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#Manual two 2d list
gradebook = [["physics", 98], ['calculus', 97], ["poetry", 85], ["history", 88]]
#print(gradebook)

#modify list several times
gradebook.append(["computer science", 100])
#print(gradebook)
gradebook.append(["visual arts", 93])
#print(gradebook)
gradebook[-1][-1] = 98
#print(gradebook)
gradebook[2].remove(85)
#print(gradebook)
gradebook[2].append("Pass")
#print(gradebook)

#add both lists together for one big list!
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
