import os
import shutil

def main():
    root_directory = '/Users/yutatokoi/github/leetcode'
    remaining_main_files = []

    # Iterate over all subdirectories in the root directory
    for subdirectory in os.listdir(root_directory):
        subdirectory_path = os.path.join(root_directory, subdirectory)

        # Check if the subdirectory name starts with a 4-digit number and if it is a directory
        if os.path.isdir(subdirectory_path) and subdirectory[:4].isdigit():
            four_digit_number = subdirectory[:4]

            # Iterate over files in the subdirectory
            for filename in os.listdir(subdirectory_path):
                file_path = os.path.join(subdirectory_path, filename)

                # Check if the file name is "main" with an extension
                if os.path.isfile(file_path) and filename.startswith("main"):
                    name, extension = os.path.splitext(filename)

                    # Rename the file to the 4-digit number with the same extension
                    new_filename = f"{four_digit_number}{extension}"
                    new_file_path = os.path.join(subdirectory_path, new_filename)
                    os.rename(file_path, new_file_path)

                    # Move the renamed file up one directory
                    shutil.move(new_file_path, os.path.join(root_directory, new_filename))

            # Check if there are any files named "main" left in the subdirectory
            for filename in os.listdir(subdirectory_path):
                if filename == "main":
                    remaining_main_files.append(os.path.join(subdirectory_path, filename))

            # Remove the subdirectory after processing
            if not remaining_main_files or not any(f.startswith(subdirectory_path) for f in remaining_main_files):
                shutil.rmtree(subdirectory_path)

    # Print out the remaining "main" files, if any
    if remaining_main_files:
        print("Remaining 'main' files:")
        for file in remaining_main_files:
            print(file)

if __name__ == "__main__":
    main()

