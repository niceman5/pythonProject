import tomllib


with open("E:\pythonProject\Test\config\config.toml", "rb") as f:
    data = tomllib.load(f)

print(data, type(data))    
print(data["title"])
print(data["owner"])
print(data["owner"]["name"])
print(data["database"]["enabled"])
print(data["database"]["temp_targets"])
print(data["database"]["temp_targets"]["cpu"])
print(data["database"]["data"])
# print(data["database"]["temp_targets"]["cpu222"]) 없으면 에러남
print(data["database"]["data"][0])
print(data["database"]["data"][0][1])

print(data["servers"])
# 그룹핑됨
print(data["servers"]["alpha"])
print(data["servers"]["beta"])
