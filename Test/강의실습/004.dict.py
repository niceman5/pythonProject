from typing import Optional

play_data = {
    "result" : "승리",
    "champ_name":"홍길동",
    "kill":50,
    "death":3    
}

# keys
for key in play_data.keys():
    print(key)

#values
for value in play_data.values():
    print(value)

#itme
for key, value in play_data.items():
    print(key, value)

tuple_a = (1,2,3,4)    

for value in tuple_a:
    print(value)

name : str = "김태훈"
name = 1
