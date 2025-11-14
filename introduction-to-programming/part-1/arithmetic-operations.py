# https://programming-25.mooc.fi/part-1/4-arithmetic-operations
# +	Addition	2 + 4	6
# -	Subtraction	10 - 2.5	7.5
# *	Multiplication	-2 * 123	-246
# /	Division (floating point result)	9 / 2	4.5
# //	Division (integer result)	9 // 2	4
# %	Modulo	9 % 2	1
# **	Exponentiation	2 ** 3	8


number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

sum = number1 + number2 + number3
print(f"The sum of the numbers: {sum}")


sum = 0

number = int(input("First number: "))
sum = sum + number

number = int(input("Second number: "))
sum = sum + number

number = int(input("Third number: "))
sum = sum + number

print(f"The sum of the numbers: {sum}")
