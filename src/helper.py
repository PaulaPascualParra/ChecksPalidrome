def read_file(file):
    try:
        with open(file) as my_file:
            data = my_file.read()
            my_file.close()
            return data

    except UnicodeDecodeError:
        print("Not an utf-8 file, can't read it. Sorry :(")
        raise
    except IsADirectoryError:
        print("Is a directory, we need a file to continue :)")
        raise
    except FileNotFoundError:
        print("Couldn't find the file, make sure you write the right path.")
        raise
    except Exception as e:
        print("Something went wrong. " + str(e))
        raise


def input_process_data(text):
    return input(text).lower() == "y"


def process_data(data):
    if input_process_data("You want to process the data on the file "
                          "(lower and upper cases as the same, no spaces or line jumps):"
                          " [y/Y for YES any other key for NO]"):
        data = data.lower().replace(' ', '').replace('\n', '')

    return data


def get_input_data():
    data = ""
    while data == "":
        try:
            file = input("Enter your file path: ")
            data = read_file(file)
        except:
            pass

    data = process_data(data)
    return data
