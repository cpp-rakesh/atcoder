'''
  Contest 200
  B - 200th ABC-200
  Rakesh Kumar --> 31/05/2021
'''

def solve():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200');
    print(n)

if __name__ == '__main__':
    solve()
