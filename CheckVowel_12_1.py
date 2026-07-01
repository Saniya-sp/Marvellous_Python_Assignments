"""Write a program which accepts one character and checks whether it is vowel or consonant.
ip = a
op = Vowel"""

def ReverseVowel(ch, vowels):
    
    for chr in vowels:
        # print(chr, ch, type(chr), type(ch))
        if ch.lower() == chr:
            return True
        
def main():
    vowels = ['a','e','i','o','u']
    char = str(input("enter a character: "))
    Ret = ReverseVowel(char, vowels)

    if Ret:
        print("Vowel")
    else:
        print("Consonant")
        
if __name__ == "__main__":
    main()