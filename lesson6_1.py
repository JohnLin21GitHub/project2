def sayHello():
    print("Hello!")

def sayHello_withName(name):
    print("Hello!"+name)

def square_area(side):
    area=side**2
    return area

def rectangle(width,height):
    area=width*height
    return(area)

if __name__=="__main__":
    sayHello_withName("John")

side=eval(input("輸入邊:"))
area=square_area(side)
print(f"邊長{side}，面積為{area}")

area=rectangle(15.5,20.9)
print(f"矩形面積為{area}")

#print(test)