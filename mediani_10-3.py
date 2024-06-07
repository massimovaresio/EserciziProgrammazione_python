"""
Si prega di rispettare i termini della licenza: https://creativecommons.org/licenses/by/4.0/
"""

def del_estremi(lista):
    del lista[0]
    del lista[-1]
    return lista
    

t = [1, 2, 3, 4]
print("Restituisco la lista tagliata senza estremi:")
print(del_estremi(t))

"""
SECONDA VERSIONE:

def mediani(lista):
    return lista[1:-1]

"""

"""
Confronto delle Due Versioni:
Caratteristica	                    del_estremi	                                            mediani

Modifica in loco	                Sì, modifica la lista originale.	                    No, crea una nuova lista.

Efficienza in tempo e spazio	    Potenzialmente più efficiente in termini                Meno efficiente in termini di memoria, ma evita effetti collaterali.
                                    di spazio, ma può causare effetti collaterali.	
                                    
Implicazioni sulla lista originale	La lista originale viene alterata permanentemente.	    La lista originale rimane invariata.

Usabilità	                        Può causare problemi se la lista è utilizzata altrove.	Più sicura in contesti in cui la lista originale deve rimanere intatta.


"""

