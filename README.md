#  RomanNumeral

A two-way **Roman numeral ↔ integer converter** with strict input checking and a test suite.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Features

- **Roman → Integer:** handles subtractive notation (`IV`, `XC`, `CM` …)
- **Integer → Roman:** greedy conversion over the standard values
- **Validation:** rejects invalid characters and illegal subtractive pairs (for example `IC` or `VX`) instead of returning a wrong answer
- **Case-insensitive** input
- **Tested:** `ConverterTest.py` runs PASS/FAIL checks on normal cases, edge cases and invalid input

## Usage

```bash
git clone https://github.com/akutsner/RomanNumeral.git
cd RomanNumeral
python CLI.py
```

```
1.Roman to Int converter? Or  2. Int to Roman converter? 1
Enter a roman numeral: mcmxciv
The roman numeral MCMXCIV is:  1994
```

Run the tests:

```bash
python ConverterTest.py
```

## Files

| File | Purpose |
|---|---|
| `Converter.py` | Conversion and validation logic |
| `CLI.py` | Interactive command-line interface |
| `ConverterTest.py` | Test script |
