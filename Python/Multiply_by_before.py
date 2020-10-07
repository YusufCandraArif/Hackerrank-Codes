'''
You are asked to multiply (n) based on the number of numbers you enter. The number of numbers will determine the number of iterations performed. (n) comes from multiplying the previous number, n = b * (a + 1)

Input Format

A single integer

.

Sample Input

4

Sample Output

1
2
6
24

'''

def multiply_before(s):
    a, b = 0, 1
    while a <= s:
        if a:
            print(b)
        a, b = a + 1, b * (a+1)

if __name__ == '__main__':
    s = input()
    result = multiply_before(s)