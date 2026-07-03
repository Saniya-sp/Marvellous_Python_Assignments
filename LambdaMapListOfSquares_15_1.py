"""Write a lambda function using map() which accepts a list of numbers and return a list of squares of each number."""

squareOfNum = lambda a : a * a            

def main():
    nums = [2, 4, 6, 8, 10]
    
    MData = list(map(squareOfNum, nums))
    
    print(MData) 

  
if __name__ == "__main__":
    main()