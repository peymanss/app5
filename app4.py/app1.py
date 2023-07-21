import random
a = input("tupe R to roll the dice")
if a=="R":
    a = random.randint(1 , 6)
    print("The number turned up is " , a)
    if a==6:
        f = input("You got 6. type R to re-roll the dice")
        b = random.randint(1 , 6)
        print(b)
        if b==6:
            k = input("You got 6. type R to re-roll the dice")
            c = random.randint(1 , 6)
            print(c)
            if c==6:
                d = random.randint(1 , 6)
                print(d)