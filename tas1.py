try:
    with open('sample.txt', 'r') as file:
        print("Contents of sample.txt:")
        print("----------------------")
        for line in file:
            print(line, end='')  
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist in the current directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
