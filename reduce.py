from functools import reduce
words = ["Python", "is", "awesome"]
sentence = reduce(lambda x,y: x+" "+y,words)
print(sentence)

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 30}
]
aged = filter(lambda x: int(x["age"]) > 20, users)

names = map(lambda x:x["name"], aged)
print(list(names))