#Exercise 3: Algorithmic Test
#Write a Python program to convert an integer to a roman numeral. Roman digits are: digits = ["M", "CM", "D", "CD”, "C", "XC", "L", "XL”, "X", "IX", "V", "IV", "I"]

class convert_int_to_roman:
    def integer_to_Roman(self, num):
        arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        roman = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

        roman_numeral = ''
        i = 0
        while  num > 0:
            for _ in range(num // arabic[i]):
                roman_numeral += roman[i]
                num -= arabic[i]
            i += 1
        return roman_numeral

a = int(input("Enter the Arabic Number = "))
obj = convert_int_to_roman().integer_to_Roman(a)

print("The Convert Integer to Roman Numeral is : ", obj)
