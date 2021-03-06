def solution(phone_book):   
    phone_book.sort(key=lambda x: x)

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:
            return False
        
    return True

'''
#Test case 1
phone_book = ["119", "97674223", "1195524421"]
#result false
'''

'''
#Test case 2
phone_book = ["123", "456", "789"]
#result true
'''

'''
#Test case 3
phone_book = ["12", "123", "1235", "567", "88"]
#result false
'''

'''
#Test case 4
phone_book = ["12", "112", "012"]
#result True
'''

#Test case 5
phone_book = ["123", "12", "13"]
#result false

print(solution(phone_book))