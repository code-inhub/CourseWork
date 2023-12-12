def find_correct(word_dict):
    correct_count = 0
    almost_correct_count = 0
    wrong_count = 0

    for correct_word, contestant_spelling in word_dict.items():
        if correct_word == contestant_spelling:
            correct_count += 1
        elif len(correct_word) == len(contestant_spelling):
            diff_count = sum(c1 != c2 for c1, c2 in zip(correct_word, contestant_spelling))
            if diff_count <= 2:
                almost_correct_count += 1
            else:
                wrong_count += 1
        else:
            wrong_count += 1

    return [correct_count, almost_correct_count, wrong_count]


word_dict = {
    "THEIR": "THEIR",
    "BUSINESS": "BISINESS",
    "WINDOWS": "WINDMILL",
    "WERE": "WEAR",
    "SAMPLE": "SAMPLE"
}
output = find_correct(  word_dict)
print(output)