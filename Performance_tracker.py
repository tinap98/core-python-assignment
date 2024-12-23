def cal_avg(marks):
    return sum(marks)/len(marks)
def top_performer(students):
    avg_marks={student:cal_avg(marks) for student,marks in students.items()}
    performer=max(avg_marks,key=avg_marks.get)
    return avg_marks,performer
n=int(input("Enter the number of students:"))
students={}
for _ in range(n):
    name=input("Enter the student's name:")
    marks=list(map(int,input(f"Enter the marks for {name} giving space inbetween:").split()))
    students[name]=marks
avg_marks,performer=top_performer(students)
print("\nAverage marks:",avg_marks)
print(f"Top performer: {performer}")