"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

def ricorsione(n, s):
    if n == 0:
        print(s)
    else:
        ricorsione(n-1, n+s)

ricorsione(3, 0)            