def count_word_occurrences(sentence):
    # Split the input sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word occurrences
    word_counts = {}

    # Iterate over each word and count its occurrences
    for word in words:
        # Increment the count for the word or set it to 1 if it's the first occurrence
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Get input sentence from the user
input_sentence = input("Enter a sentence: ")

# Count word occurrences in the input sentence
word_occurrences = count_word_occurrences(input_sentence)

# Print the dictionary containing unique words and their occurrences
print("Word occurrences:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")