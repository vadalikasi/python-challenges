from itertools import product
from numpy import max
import sys

'''
Question:

You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and . 
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

Constraints

 
 
 

Output Format

Output a single integer denoting the value .

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206

'''


def custom_error_handling():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': exc_traceback.tb_frame.f_code.co_filename,
        'line_no': exc_traceback.tb_lineno,
        'name': exc_traceback.tb_frame.f_code.co_name,
        'type': exc_type.__name__,
        # 'message': exc_traceback._some_str()
    }
    return traceback_details




if __name__ == '__main__':
    ''''''
    try:
        input_list = input().split()
        items, m = int(input_list[0]), int(input_list[1])
        # sum = 0
        i_li = []
        for i in range(items):
            i_li.append([int(num) * int(num) for num in (input().split())][1:])
        result = list(map(lambda x: sum([value for value in x]) % m, product(*i_li)))
        print(max(result))
    except IndexError as e:
        print("Input arguments were not provided accurately : " + str(e))
        print(custom_error_handling())
    except Exception as e:
        print("Exception occurred : " + str(e))
