# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("Hello, Hello world.\n")
        file.write("wassupp\n")
        file.write("Its a beautiful day\n")
except Exception as e:
    print("Error occurred while creating or writing to the file:", e)

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied while reading the file.")
except Exception as e:
    print("Error occurred while reading the file:", e)

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("This is line 4 added in append mode.\n")
        file.write("Another line with some more content.\n")
        file.write("Appending the final line.\n")
except Exception as e:
    print("Error occurred while appending to the file:", e)
finally:
    print("File handling completed.")

