"""Write a lambda function using filter() which accepts list of strings and 
returns the strings having lenght greater than five"""


CheckStrLenght = lambda strs: strs if len(strs) > 5 else False

def main():
    Data = ['hi','saniya', 'how','are','classes','going','great?','happy!!']
  
    print("Input data is :",Data)

    FData = list(filter(CheckStrLenght, Data))  
    print("FData is: ",FData)


if __name__ == "__main__":
    main()

