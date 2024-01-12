# Same as pi_to_n_digit, but swapped trunicated number

import math

def truncate(f, n):
    if n > 100:
        n = 100
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        # What does this . do in the string?
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def main():
    num = int(input())
    newPi = truncate(math.e, num)
    print(newPi)

main()