

intToNumeral = {
    int (1) : "I",
    int (4) : "IV",
    int (5) : "V",
    int (9) : "IX",
    int (10) : "X",
    int (40) : "XL",
    int (50) : "L",
    int (90) : "XC",
    int (100) : "C",
    int (400) : "CD",
    int (500) : "D",
    int (900) : "CM",
    int (1000) : "M",
}



numeralToInt = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Allowed subtractive pairs
validPairs = {
    "I": ["V", "X"],
    "X": ["L", "C"],
    "C": ["D", "M"]
}

def romanToInt(s):
    s = s.upper()
    total = 0
    i = 0

    while i < len(s):
        if s[i] not in numeralToInt:
            return None

        curr = numeralToInt[s[i]]


        if i + 1 < len(s):
            if s[i + 1] not in numeralToInt:
                return None

            next_val = numeralToInt[s[i + 1]]


            if curr < next_val:


                if s[i] not in validPairs or s[i + 1] not in validPairs[s[i]]:
                    return None

                total = total + (next_val - curr)
                i = i + 2
            else:
                total = total + curr
                i = i + 1
        else:
            total = total + curr
            i = i + 1

    return total


def intToRoman(s):
    s = int(s)
    total = 0
    i = 0

    while i < len(s):

