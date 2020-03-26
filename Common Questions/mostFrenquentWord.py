"""
“One fish two fish red fish blue fish”
Write a function that will return the most frequent word in the sentence. 
Write some test cases for this as well.
"""

def most_frequent(bag_of_words):
    words_dict = {}
    split_words = bag_of_words.split()

    # loop through list of words
    for word in split_words:
        # if word is not in the dict append the word
        if word not in words_dict:
            words_dict[word] = 1
        else: 
            # otherwise add
            words_dict[word] += 1

    return max(words_dict, key=lambda key: words_dict[key])



chunk_of_words = 'One fish two fish red fish blue fish'
get_frequent_word = most_frequent(chunk_of_words)
print(get_frequent_word)