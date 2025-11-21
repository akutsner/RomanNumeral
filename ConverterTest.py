

from Converter import romanToInt




def run_test(value, expected):
    try:
        result = romanToInt(value)
        if result == expected:
            print("PASS:", value, "=>", result)
        else:
            print("FAIL:", value, "=>", result, "(expected", expected, ")")
    except Exception as e:
        print("ERROR:", value, "raised", type(e).__name__, e)


def main():
    print("=== Testing romanToInt ===")

    # Basic numerals
    run_test("I", 1)
    run_test("V", 5)
    run_test("X", 10)
    run_test("L", 50)
    run_test("C", 100)
    run_test("D", 500)
    run_test("M", 1000)

    # Common combinations
    run_test("II", 2)
    run_test("III", 3)
    run_test("IV", 4)
    run_test("VI", 6)
    run_test("IX", 9)
    run_test("XI", 11)
    run_test("XIV", 14)
    run_test("XIX", 19)
    run_test("XX", 20)
    run_test("XL", 40)
    run_test("XC", 90)
    run_test("CD", 400)
    run_test("CM", 900)

    # Larger numbers
    run_test("LVIII", 58)  # 50 + 5 + 3
    run_test("MCMXCIV", 1994)  # 1000 + 900 + 90 + 4
    run_test("MMXXV", 2025)

    # Lower/upper-case handling
    run_test("mcm", 1900)

    # Illegal input
    run_test("A", None)
    run_test("IC", None)
    run_test("VX", None)


if __name__ == "__main__":
    main()
