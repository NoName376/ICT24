sentence = input("Enter a sentence: ").strip()
if sentence:
    words = sentence.split(',')
    unique_words = set(words)
    print(f"Number of unique words: {len(unique_words)}")
else:
    print("Please enter a non-empty sentence.")
