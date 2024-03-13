# sleep pattern printing


from time import sleep

for i in range(9):
    for j in range(i+1):
        print("*", end=" ")
        sleep(0.9)
    print()