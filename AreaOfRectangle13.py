"""Write a program which accepts length and width of rectangle and prints area"""


def areaOfRectangle(lenght, width):
    
    return lenght * width

def main():

    lenght = int(input("enter lenght of rectangle: "))
    width = int(input("enter width of rectangle: "))
    Ret = areaOfRectangle(lenght, width)
    
    print("Area of rectangle is :",Ret)
    

if __name__ == "__main__":
    main()