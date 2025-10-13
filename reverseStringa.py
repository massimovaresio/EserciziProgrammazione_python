def reverseStringa(s):
    lunghezza = len(s)
    i = lunghezza - 1
    while i >= 0:
        lettera = s[i]
        print(lettera)
        i = i - 1

stringa = input("Inserisci la parola che verrà letta al contrario: ")
reverseStringa(stringa)       

