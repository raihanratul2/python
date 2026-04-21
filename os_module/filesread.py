from datetime import datetime

print("how many cycle? : ")
cycle = int(input())
for i in range(cycle):
    print("give some imput:")
    data = str(input())

    with open("log.txt","a") as file:
        file.write(
            f"{i}-{data}-{datetime.now().strftime("%H:%M:%S")} ,\n"
        )
with open("log.txt","r") as file:
    lines = file.readlines()
    for i in lines:
        print(i)

