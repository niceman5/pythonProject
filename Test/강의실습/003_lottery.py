import random

lotto_num = []  # 빈 로또 번호 리스트 
  
def getRndNumber():
    number = random.randint(1, 45)
    return number


while True:    
    random_number = getRndNumber()    
    if random_number not in lotto_num:
        lotto_num.append(random_number)     
        # print(lotto_num)   
        if len(lotto_num) >= 6:
            break        
    
lotto_num.sort()    
print(lotto_num)