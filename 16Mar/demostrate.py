def count_ways(amount, denomination_list):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denomination_list) == 0:
        return 0
    return count_ways(amount - denomination_list[0], denomination_list) + count_ways(amount, denomination_list[1:])
amount_1=int(input())
input_string=input()
denomination_list_1=eval(input_string)
print(count_ways(amount_1, denomination_list_1))
amount_1 = 4
denomination_list_1 = [1, 2, 3]
print(count_ways(amount_1, denomination_list_1))

amount_2 = 10
denomination_list_2 = [10, 5, 1]
print(count_ways(amount_2, denomination_list_2))

amount_3 = 50
denomination_list_3 = [50, 25, 10, 5]
print(count_ways(amount_3, denomination_list_3)) 
def find_10_substrings(number):
    substrings = []
    for i in range(len(number)):
        for j in range(i+1, len(number)+1):
            substring = number[i:j]
            if sum(int(digit) for digit in substring) == 10:
                substrings.append(substring)
    return substrings
number = "3523014"
substrings = find_10_substrings(number)
print(substrings) 