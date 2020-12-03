with open("2020/day_02/input.txt",'r') as input_file:
    passwords = input_file.read()

valid_pwd = 0

def xor (a : bool, b : bool):
    return (a and not b) or (not a and b)

for password_line in passwords.splitlines():
    password_array = password_line.partition(' ')
    (pos1, _, pos2) = password_array[0].partition('-')
    (char, _, pwd) = password_array[2].partition(': ')

    if xor(pwd[int(pos1) - 1] == char, pwd[int(pos2) - 1] == char):
        valid_pwd += 1

print(valid_pwd)