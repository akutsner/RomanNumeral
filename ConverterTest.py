from Converter import romanToInt, intToRoman


def run_test(func_name, value, expected):
    try:
        if func_name == "romanToInt":
            result = romanToInt(value)
        else:
            result = intToRoman(value)

        if result == expected:
            print("PASS:", value, "=>", result)
        else:
            print("FAIL:", value, "=>", result, "(expected", expected, ")")

    except Exception as e:
        print("ERROR:", value, "raised", type(e).__name__, e)


def test_romanToInt():
    print("=== Testing romanToInt ===")

    # Basic numerals
    run_test("romanToInt", "I", 1)
    run_test("romanToInt", "V", 5)
    run_test("romanToInt", "X", 10)
    run_test("romanToInt", "L", 50)
    run_test("romanToInt", "C", 100)
    run_test("romanToInt", "D", 500)
    run_test("romanToInt", "M", 1000)

    # Common combinations
    run_test("romanToInt", "II", 2)
    run_test("romanToInt", "III", 3)
    run_test("romanToInt", "IV", 4)
    run_test("romanToInt", "VI", 6)
    run_test("romanToInt", "IX", 9)
    run_test("romanToInt", "XI", 11)
    run_test("romanToInt", "XIV", 14)
    run_test("romanToInt", "XIX", 19)
    run_test("romanToInt", "XX", 20)
    run_test("romanToInt", "XL", 40)
    run_test("romanToInt", "XC", 90)
    run_test("romanToInt", "CD", 400)
    run_test("romanToInt", "CM", 900)

    # Larger numbers
    run_test("romanToInt", "LVIII", 58)
    run_test("romanToInt", "MCMXCIV", 1994)
    run_test("romanToInt", "MMXXV", 2025)

    # Lowercase handling
    run_test("romanToInt", "mcm", 1900)

    # Invalid inputs
    run_test("romanToInt", "A", None)
    run_test("romanToInt", "IC", None)
    run_test("romanToInt", "VX", None)


def test_intToRoman():
    print("\n=== Testing intToRoman ===")

    # Basic numbers
    run_test("intToRoman", 1, "I")
    run_test("intToRoman", 3, "III")
    run_test("intToRoman", 4, "IV")
    run_test("intToRoman", 9, "IX")
    run_test("intToRoman", 10, "X")
    run_test("intToRoman", 40, "XL")
    run_test("intToRoman", 90, "XC")
    run_test("intToRoman", 400, "CD")
    run_test("intToRoman", 900, "CM")

    # Larger numbers
    run_test("intToRoman", 58, "LVIII")
    run_test("intToRoman", 1994, "MCMXCIV")
    run_test("intToRoman", 2025, "MMXXV")
    run_test("intToRoman", 3999, "MMMCMXCIX")  # highest typical Roman numeral


def main():
    test_romanToInt()
    test_intToRoman()


if __name__ == "__main__":
    main()
