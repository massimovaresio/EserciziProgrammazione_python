def ricorsione(n, s):
    if n == 0:
        print(s)
    else:
        ricorsione(n-1, n+s)

ricorsione(3, 0)            