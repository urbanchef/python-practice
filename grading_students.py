def grading_students(grades):
    for idx, grade in enumerate(grades):
        if grade < 38:
            continue
        remainder = grade % 5
        multiple_of_five = 5 - remainder + grade
        difference = abs(grade - multiple_of_five)
        if difference < 3:
            grades[idx] = multiple_of_five
    return grades


if __name__ == "__main__":
    grades = []
    grading_students(grades)
