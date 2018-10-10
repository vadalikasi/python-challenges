''' This program identified every nth character in a given string'''
import sys


def my_parser(user_input, number):
    output = []
    for i in range(number - 1, len(user_input), number):
        output.append(user_input[i])
    return ''.join(output)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        user_text = sys.argv[1]
        user_number = int(sys.argv[2])
        print(my_parser(user_text, user_number))
    else:
        print("invalid arguments")
