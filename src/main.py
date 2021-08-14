import helper
import function

if __name__ == '__main__':
    # todo: create an interface with pyqt
    input_data = helper.get_input_data()
    print(function.is_palindrome_reverse(input_data))
    print(function.is_palindrome_queue(input_data))
    print(function.is_palindrome_optimized(input_data))
