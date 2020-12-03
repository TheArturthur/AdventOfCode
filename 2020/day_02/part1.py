with open("2020/day_02/input.txt",'r') as input_file:
    passwords = input_file.read()

valid_pwd = 0
for password_line in passwords.splitlines():
    password_array = password_line.partition(' ')
    (min_rep, _, max_rep) = password_array[0].partition('-')
    (char, _, pwd) = password_array[2].partition(': ')

    if pwd.count(char) <= int(max_rep) and pwd.count(char) >= int(min_rep):
        valid_pwd += 1

print(valid_pwd)