def solution(phone_book):   
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:
            return False
        
    return True


#Test case 1
phone_book = ["119", "97674223", "1195524421"]
#result false

print(solution(phone_book))