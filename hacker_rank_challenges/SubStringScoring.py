from collections import defaultdict


# import datetime as dt
def find_all(sub, s):
    return [i for i in range(len(s)) if s.startswith(sub, i)]


def gen_sub_list(s):
    sub_list = defaultdict(int)
    score = {'Stuart': 0, 'Kevin': 0}
    test = 'AEIOU'
    fall = find_all
    length = len
    # print(dt.datetime.now())
    for i in range(length(s)):
        for j in range(i + 1, length(s) + 1):
            sub_text = s[i:j]
            if sub_text not in sub_list:
                sub_list[sub_text] = length(fall(sub_text, s))
                if sub_text[0] in test:
                    score['Kevin'] += sub_list[sub_text]
                else:
                    score['Stuart'] += sub_list[sub_text]
    # print(dt.datetime.now())
    return score


def minion_game(s):
    # print(dt.datetime.now())
    # s='BANANA'
    result = gen_sub_list(s)
    # print(dt.datetime.now())
    if result['Stuart'] > result['Kevin']:
        print('Stuart ' + str(result['Stuart']))
    elif result['Stuart'] < result['Kevin']:
        print('Kevin ' + str(result['Kevin']))
    else:
        print('Draw')


if __name__ == '__main__':
    s_input = input()
    minion_game(s_input)
