def rotation(user_list, rotation_count):
    '''
    :param user_list:
    :param rotation_count:
    :return: list

    rotate the list left if rotation count is less than or equal to half. Otherwise rotate right if we get
    same result in less no of rotations. return same list if full rotation is required.
    '''

    if rotation_count > 0:
        for i in range(rotation_count):
            temp = user_list.pop(0)
            user_list.append(temp)
    elif rotation_count < 0:
        for i in range(abs(rotation_count)):
            temp = user_list.pop()
            user_list.insert(0, temp)
    return user_list


if __name__ == '__main__':
    user_input_size = list(map(int, input().split()))
    user_input_array = list(map(int, input().rstrip().split()))
    length = len(user_input_array) / 2
    if user_input_size[1] > length:
        rotation(user_input_array, user_input_size[1])
    else:
        rotation(user_input_array, user_input_size[1] - user_input_size[0])
    print(user_input_array)
