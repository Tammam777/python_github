if __name__ == '__main__':
    records = []  # قائمة لتخزين بيانات الطلاب
    for _ in range(int(input("أدخل عدد الطلاب: "))):
        name = input("أدخل اسم الطالب: ")
        score = float(input("أدخل درجة الطالب: "))
        records.append([name, score])

    # إيجاد ثاني أدنى درجة
    scores = sorted(set([record[1] for record in records]))
    second_lowest_score = scores[1]

    # إيجاد الطلاب الحاصلين على ثاني أدنى درجة
    students_with_second_lowest = [record[0] for record in records if record[1] == second_lowest_score]

    # ترتيب الأسماء أبجديًا
    students_with_second_lowest.sort()

    # طباعة الأسماء
    for student in students_with_second_lowest:
        print(student)
    print(students_with_second_lowest)    
