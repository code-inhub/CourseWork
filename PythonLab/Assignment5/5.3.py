
def find_word_with_max_frequency(text):

    words = text.lower().split()
    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    max_freq = max(word_freq.values())
    max_freq_words = [word for word, freq in word_freq.items() if freq == max_freq]

    word_with_max_freq = max(max_freq_words, key=lambda x: (len(x), x))

    return f"{word_with_max_freq} {max_freq}"

input_text1 = "Work like you do not need money love like you have never been hurt and dance like no one is watching"
output1 = find_word_with_max_frequency(input_text1)
print(f"Expected Output for Sample Input 1: {output1}")

input_text2 = "Courage is not the absence of fear but rather the judgement that something else is more important than fear"
output2 = find_word_with_max_frequency(input_text2)
print(f"Expected Output for Sample Input 2: {output2}")
