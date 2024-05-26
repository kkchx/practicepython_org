def reverse_word_order(sentence):
    words = sentence.split()
    words_reversed = []
    for i in range(len(words),1,-1):
        words_reversed.append(words[i])
    return words_reversed

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    sentence = reverse_word_order(user_input)
    print(sentence)


# TODO
# 1. Ask user to enter the sentence
# 2. Send a sentence to a function
# 3. finish a function to return a reversed sentence