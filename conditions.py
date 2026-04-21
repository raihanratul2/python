
if __name__ == '__main__':
    n = int(input().strip())
    if 1 < n and n < 100:
        if n%2 == 0:
            print("Not Weird")
        elif n%2 == 1:
            print("Weird")
    else:
        print(f"{n} is not bigger than 1")