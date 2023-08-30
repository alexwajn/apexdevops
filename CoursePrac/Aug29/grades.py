def main():
    grades = [0,0,0,0,0]
    grades[0] = 7
    grades[1] = 6
    grades[2] = 4
    grades[3] = 8
    grades[4] = 5
    sum = 0
    for grade in grades:
        sum = sum + grade
    print("Sum of grades:_", sum)
    print("Average:_", sum / len(grades))


if __name__ == '__main__':
    main()
