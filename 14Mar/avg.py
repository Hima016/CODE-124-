list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def freq(list_of_marks):
    l=[]
    for i in range(26):
        l.append(list_of_marks.count(i))
    return l
print(freq(list_of_marks))

