def grades_list() -> list[int]:
    grade = 0
    grades_lst = []

    while not grade:
        try:
            while True:
                grade = int(input("enter grade"))
                if grade == -99:
                    break
                elif 0 <= grade <= 100:
                    grades_lst.append(grade)
                else:
                    continue
        except ValueError:
            print("enter a number")

        return grades_lst


print(grades_list())