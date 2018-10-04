from itertools import product
from numpy import max
import sys


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
