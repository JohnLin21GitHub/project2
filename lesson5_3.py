#主要執行的程式
'''
this is a game
just lesson
'''
import random

min=1
max=10
count = 0
random_value=random.randint(1,10)
print(random_value)

if __name__=="__main__":
    print("====猜數字====")
    while True:
        keyin = int(input(f"please input {min}~{max} : "))
        count += 1
        if keyin>=min and keyin<=max:
            if keyin == random_value:
                print(f"answer is {random_value}")
                break
            elif keyin > random_value:
                print("小一點")
                max = keyin-1
            elif keyin < random_value:
                print("大一點")
                min = keyin+1
        else:
            print("超過範圍")

    print(f"game over, 猜了{count}次")
print(keyin)
