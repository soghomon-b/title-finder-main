def new_line(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()

        # Add an empty line after each line
        modified_lines = [line.strip() + '\n\n' for line in lines]

        with open(input_file_path, 'w') as file:
            file.writelines(modified_lines)

        print(f"Empty lines added to {input_file_path}")

    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    new_line(file_path)
