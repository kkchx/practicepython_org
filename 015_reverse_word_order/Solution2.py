def reverse_word_order(sentence):
    words = sentence.split()
    words_reversed = []
    for i in range(len(words),0,-1):
        words_reversed.append(words[i])

    reversed_sentence = " ".join(reversed(words_reversed))


# TODO
# 1. Ask user to enter the sentence
# 2. Send a sentence to a function
# 3. finish a function to return a reversed sentence