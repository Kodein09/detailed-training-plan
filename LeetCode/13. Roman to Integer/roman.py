def roman_to_integer(n):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    total = 0
    for i in range(len(n) - 1):
        print(roman[n[i]])
        if roman[n[i]] < roman[n[i + 1]]:
            total -= roman[n[i]]
        else:
            total += roman[n[i]]
    return total + roman[n[-1]]
print(roman_to_integer('MCMXCIV'))