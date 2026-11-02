def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


text = input("Enter a sentence: ")
print(reverse_words(text))
