def find_correct(word_dict):
    correct_count = 0
    almost_correct_count = 0
    wrong_count = 0
    
    for word, contestant_spelling in word_dict.items():
        if word == contestant_spelling:
            correct_count += 1
        elif abs(len(word) - len(contestant_spelling)) > 2:
            wrong_count += 1
        else:
            wrong_letters = sum([1 for i in range(len(word)) if word[i] != contestant_spelling[i]])
            if wrong_letters <= 2:
                almost_correct_count += 1
            else:
                wrong_count += 1
    
    return [correct_count, almost_correct_count, wrong_count]
dict1={"THEIR":"THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
a=find_correct(dict1)
print(a)