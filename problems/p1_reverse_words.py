import string

def reverse_words(sentence):
    words = sentence.split()
    words = [word.strip(string.punctuation) for word in words]
    return " ".join(words[::-1])

text = input("Enter a sentence: ")
print(reverse_words(text))
