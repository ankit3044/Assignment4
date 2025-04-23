def main():
    initial_data = input("Enter the initial text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(initial_data + '\n')  
    print("Initial data written to output.txt successfully!")
    additional_data = input("Enter additional text to append to the file: ")
    with open('output.txt', 'a') as file:
        file.write(additional_data + '\n')
    print("Additional data appended to output.txt successfully!")
    print("\nFinal content of output.txt:")
    print("--------------------------------")
    with open('output.txt', 'r') as file:
        content = file.read()
        print(content)
    print("--------------------------------")
if __name__ == "__main__":
    main()
