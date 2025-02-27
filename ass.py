while True:
    a = int(input("вкажіть число від 1 до 20 "))
    if 1 <= a <= 20:
        if a == 12:
            print("ви вгадали число")
            break
        else:
            print("ви не вгадали число")
    else:
        print("число повинно бути в діапазоні від 1 до 20")


