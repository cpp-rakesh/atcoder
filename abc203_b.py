'''
  Contest 203
  B - AtCoder Condominium
  Rakesh Kumar --> 15/06/2021
'''

def solve():
    n,k = map(int, input().split())
    s = 0
    for i in range(1, n + 1):
        s += k * (100 * i)
    s += n * (k * (k + 1) >> 1)
    print(s)

if __name__ == '__main__':
    solve()
