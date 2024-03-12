def count_text_stats(text):
    # Counting words, characters, and lines
    words = len(text.split())
    characters = len(text)
    lines = text.count('\n') + 1  # Adding 1 to count the last line

    # Displaying the results
    print("Number of words:", words)
    print("Number of characters:", characters)
    print("Number of lines:", lines)

# Get user input
user_text = input("Enter your text: ")

# Call the function with the user input
count_text_stats(user_text)
