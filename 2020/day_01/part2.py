with open("2020/day_01/input.txt",'r') as input:
    data = input.read().splitlines()

found = False
for num1 in data:
    for num2 in data:
        for num3 in data:
            if int(num1) + int(num2) + int(num3) == 2020:
                print(int(num1) * int(num2) * int(num3))
                found = True
                break
        if found:
            break
