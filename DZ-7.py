grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]]
student = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list = sorted(student)

#  без использования циклов:
average_score = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),
                sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
print(average_score)
dict_score = {student_list[0]: average_score[0], student_list[1]: average_score[1], student_list[2]: average_score[2],
              student_list[3]: average_score[3], student_list[4]: average_score[4],}
print(dict_score)

# С использованием циклов:
dict_score = {}
i = 0
while i < (len(grades)):
    average_score[i] = sum(grades[i])/len(grades[i])
    dict_score.update({student_list[i]: average_score[i],})
    i=i+1
print(average_score)
print(dict_score)


