import os

def read_until_dot(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            first_dot_index = data.find('.')
            if first_dot_index != -1:
                result_string = data[:first_dot_index]
            else:
                result_string = data
            return result_string
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def iterate_file(directory_path : str) -> list:
    first_sentence = []
    for file in os.listdir(directory_path):
        if file[0] != ".":
            m = read_until_dot(os.path.join(directory_path, file))
            first_sentence.append(m)
    with open("C:\\Users\\soghm\\OneDrive\\Documents\\GitHub\\title-finder\\evaluation\\first_sentence.txt" , "w" ) as sentence:
        for i in first_sentence: 
            sentence.write(i + '\n')
        
    return first_sentence


title = iterate_file("C:\\Users\\soghm\\OneDrive\\Documents\\GitHub\\title-finder\\evaluation_data\\title")
no_title = iterate_file("C:\\Users\\soghm\\OneDrive\\Documents\\GitHub\\title-finder\\evaluation_data\\no_title")

print(title)
print(no_title)