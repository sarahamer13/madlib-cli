import sys
import re

# class QuitGameException(Exception):
#     pass

# function explaining the game 
def print_welcome_message():
    print("Welcome to the Madlibs Game!")
    print("You will be asked to input some words to play the game.")
    print("When done, you'll receive a funny story!")
    print("Your completed madlibs will be saved in a filled_template.txt file.")
    print("To exit at any time, type 'x' and press enter.")

# function to open and read the file
def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            template_content = file.read().strip()
            print(f"Template content:\n{template_content}")
            return template_content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {file_path}")

# function ti find placeholders in the provided template and replace them with curly brackets
def parse_template(template):
    # Pattern to match placeholders like '{}' or '<>'
    # raw string, closing quote, \ escape the { character
    #.*? march as few characters as possible while allowing the overall pattern to match
    # | match anything in curly or brackets
    # [.*?\] this part of the pattern matches text enclosed in square brackets []. Similar to the curly braces part,
    # \: The backslash escapes the [ character to match a literal [.
    #.*?: This part matches any character zero or more times

    pattern = r"\{.*?\}|\[.*?\]"

    # Find all placeholders
    language_parts = re.findall(pattern, template)

    # Replace placeholders with '{}'
    parsed_template = re.sub(pattern, "{}", template)

    return parsed_template, language_parts

# function iterate over the list of placeholders, it prompts the user for input for each and return a list of these inputs
def get_user_inputs(language_parts):
    user_inputs = []
    for part in language_parts:
        user_input = input(f"Enter {part[1:-1]}: ")
        if user_input.lower() == 'x':
            exit_game()
        user_inputs.append(user_input)
    return user_inputs

# function print and exit message
def exit_game():
    print("Exiting the game. Goodbye!")
    sys.exit(0)

# function merge take a template and a list of user inputs as arguments
# the placeholders will be substitute it with the values from the user_input
def merge(template, user_inputs):
    print("Merging template with user inputs...")
    merged = template.format(*user_inputs)
    print("Merged content:", merged)
    return merged

# function print the completed madlib
def display_completed_madlib(completed_madlib):
    print("\n=== Completed Madlib ===\n")
    print(completed_madlib)

# function to write the completed madlib to a file in the assets folder
def write_to_file(completed_madlib, output_file_path):
    try:
        # Adjust the path to point to the 'assets' folder
        full_path = f'assets/{output_file_path}'
        
        with open(full_path, 'w') as file:
            file.write(completed_madlib)
        print(f"\nCompleted Madlib has been saved to {full_path}")
    except IOError as e:
        print(f"Error saving file: {e}")

# This is the main thing to call functions
def main():
    try:
        print_welcome_message()
        template_path = input("Enter the path to the Madlib template file: ")

        # Read template file
        template = read_template(template_path)

        # Parse template
        parsed_template, language_parts = parse_template(template)

        # Collect user inputs
        user_inputs = get_user_inputs(language_parts)

        # Merge template and user inputs
        completed_madlib = merge(parsed_template, user_inputs)

        # Display completed Madlib
        display_completed_madlib(completed_madlib)

        # Write the completed Madlib to a file
        write_to_file(completed_madlib, 'filled_template.txt')

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function only execute if the script is run directly 
if __name__ == "__main__":
    main()
