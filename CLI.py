import Converter
def romantoint():
    quit = True
    while quit == True:
        roman = str(input("Enter a roman numeral: ")).upper()
        final = Converter.romanToInt(roman)
        print(f"The roman numeral {roman} is: ", final)

        result = str(input("Would you like to quit (y/n): ")).upper()
        if result == "Y":
            quit = False

def inttoroman():
    quit = True
    while quit == True:
        number = str(input("Enter a number: ")).upper()
        final = Converter.intToRoman(number)
        print(f"The roman numeral {number} is: ", final)

        result = str(input("Would you like to quit (y/n): ")).upper()
        if result == "Y":
            quit = False


def main():
    quit =  True
    while quit == True:
        roman =  str(input("1.Roman to Int converter? Or  2. Int to Roman converter?")).upper()
        if roman == "1":
            romantoint()
        else:
            inttoroman()





        result = str(input("Would you like to quit (y/n): ")).upper()
        if result == "Y":
            quit = False


main()