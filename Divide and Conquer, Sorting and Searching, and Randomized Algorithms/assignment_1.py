# Question 1 In this programming assignment you will implement one or more of the integer multiplication algorithms
# described in lecture.

# To get the most out of this assignment, your program should restrict itself to multiplying only pairs of
# single-digit numbers.  You can implement the grade-school algorithm if you want, but to get the most out of the
# assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

# So: what's the product of the following two 64-digit numbers?
# 3141592653589793238462643383279502884197169399375105820974944592
# 2718281828459045235360287471352662497757247093699959574966967627

# Answer:
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

def main():
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(num1, num2))


def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    else:
        n = max(len(str(num1)), len(str(num2)))
        m = n // 2
        a = num1 // 10 ** m
        b = num1 % 10 ** m
        c = num2 // 10 ** m
        d = num2 % 10 ** m
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_bc = karatsuba(a + b, c + d) - ac - bd
        return ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd


if __name__ == "__main__":
    main()
