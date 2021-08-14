import helper


def is_palindrome_optimized(name):
    length_name = len(name)
    middle_point_name = int(length_name / 2)
    for initial_pointer, final_pointer in zip(range(0, middle_point_name),
                                              range(length_name - 1, middle_point_name - 1, -1)):
        if name[initial_pointer] != name[final_pointer]:
            return False
    return True


def is_palindrome_queue(name):
    queue = []
    length_name = len(name)
    index = 0
    while index < int(length_name / 2):
        queue.append(name[index])
        index += 1

    index += length_name % 2

    while index < length_name:
        if queue.pop() != name[index]:
            return False
        index += 1

    return True


def is_palindrome_reverse(name):
    length_name = len(name)
    s1 = name[:length_name // 2]
    s2 = name[(length_name // 2) + length_name % 2:]
    s2 = s2[::-1]
    return s1 == s2


if __name__ == '__main__':
    # todo: large files
    # todo: create tests
    # todo: create an interface with pyqt
    # todo: create a git
    input_data = helper.get_input_data()
    print(is_palindrome_reverse(input_data))
    print(is_palindrome_queue(input_data))
    print(is_palindrome_optimized(input_data))
