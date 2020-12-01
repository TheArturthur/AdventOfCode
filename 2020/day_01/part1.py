with open("2020/day_01/input.txt",'r') as input:
    data = input.read().splitlines()

for num1 in data:
    for num2 in data:
        if int(num1) + int(num2) == 2020:
            print(int(num1)*int(num2))
            break
