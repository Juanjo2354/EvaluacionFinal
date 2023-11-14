def convert_ascii(letter):
    result = ord(letter)
    return result

def convert_binary(num):
    result = bin(num)
    return result


def menu():
    print("=============\nMenu\n=============\n 1. Character\n 2. Word")
    option = int(input("Please select an option to convert into binary: "))
    
    if option == 1:
        chosenLetter = input("Write the letter: ")
        ascii_num = convert_ascii(chosenLetter)
        print("=============\nResults\n=============\n")
        print(
            "ASCII character value of", chosenLetter, "is", ascii_num ,
            "and representation of", chosenLetter, "in a byte is", convert_binary(ascii_num)
            )
    
    elif option == 2:
        chosenWord = input("Write the word: ")
        binaryWord = []
        print("=============\nResults\n=============\n")
        for i in chosenWord:
            ascii_num = convert_ascii(i)
            convertion = convert_binary(ascii_num)
            print(
                "ASCII character value of", i, "is", ascii_num ,
                "and representation of", i, "in a byte is", convertion 
                )
            binaryWord.append(convertion)
        print(" ".join(binaryWord))

menu()






