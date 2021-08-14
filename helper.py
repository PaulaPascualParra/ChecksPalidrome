def read_file(file):
    try:
        with open(file) as my_file:
            data = my_file.read()
            my_file.close()
            return data

    except UnicodeDecodeError:
        print("Not an utf-8 file, can't read it. Sorry :(")
        return False
    except IsADirectoryError:
        print("Is a directory, we need a file to continue :)")
        return False
    except FileNotFoundError:
        print("Couldn't find the file, make sure you write the right path.")
        return False
    except Exception as e:
        print("Something went wrong. " + str(e))
        return False


def process_data(data):
    if input("You want to process the data on the file: [y/Y for YES rest for NO]").lower() == "y":
        if input("Consider lower and uper cases as the same: [y/Y for YES rest for NO]").lower() == "y":
            data = data.lower()
        if input("Remove spaces: [y/Y for YES rest for NO]").lower() == "y":
            print("hi")
            data = data.replace(' ', '')
        if input("Remove line jumps: [y/Y for YES rest for NO]").lower() == "y":
            data.replace('\n', '')
    return data


def get_input_data():
    data = False
    while not data:
        file = input("Enter your file path: ")
        data = read_file(file)

    data = process_data(data)
    return data