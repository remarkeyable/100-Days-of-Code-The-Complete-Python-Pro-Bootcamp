# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#divide by n

height = 0
divide = (n + 1)

for tangkad in student_heights:
 height = height + tangkad

total = round(height / divide) 

print(total)
