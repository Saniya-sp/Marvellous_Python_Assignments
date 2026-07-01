"""Write a program which accepts radius of circle and prints area of circle"""

def areaOfCircle(radius):
    
    return radius * radius * 3.142

def main():

    radius = int(input("enter radius of circle: "))
    
    Ret = areaOfCircle(radius)
    
    print("Area of rectangle is :",Ret)
    

if __name__ == "__main__":
    main()
