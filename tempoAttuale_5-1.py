import time

# Ottieni il tempo attuale in secondi dal "tempo zero" (1 gennaio 1970)
current_time = time.time()
print(current_time) # Stampa il tempo attuale nel formato originario: La funzione time.time() restituisce il tempo attuale come numero di secondi (con parte decimale) trascorsi dal "tempo zero".

# Calcola il numero di giorni trascorsi
days = int(current_time // (24 * 3600))
# La divisione intera (//) ci dà il numero di giorni interi trascorsi.
# Dopo aver calcolato i giorni, il tempo che rimane (espresso in secondi) deve essere suddiviso ulteriormente in ore, minuti e secondi.

# Calcola il numero di secondi rimanenti dopo aver sottratto i giorni interi
remaining_seconds = current_time % (24 * 3600) # Rappresenta il numero di secondi che non formano un giorno intero e sono quindi da considerare per il calcolo delle ore.
# L'operatore modulo (%) ci dà il resto della divisione, cioè i secondi rimanenti.

# Calcola il numero di ore rimanenti
hours = int(remaining_seconds // 3600)
# Dividiamo i secondi rimanenti per 3600 per ottenere il numero di ore intere rimanenti.

# Calcola il numero di secondi rimanenti dopo aver sottratto le ore intere
remaining_seconds %= 3600
# Usiamo di nuovo l'operatore modulo per ottenere i secondi rimanenti dopo aver sottratto le ore intere.

# Calcola il numero di minuti rimanenti
minutes = int(remaining_seconds // 60)
# Dividiamo i secondi rimanenti per 60 per ottenere il numero di minuti interi rimanenti.

# Calcola il numero di secondi rimanenti dopo aver sottratto i minuti interi
seconds = int(remaining_seconds % 60)
# Usiamo di nuovo l'operatore modulo per ottenere i secondi rimanenti dopo aver sottratto i minuti interi.

# Stampa i risultati
print(f"Giorni trascorsi dal 'tempo zero': {days}")
print("Tempo/orario corrente:")
print(f"Ore: {hours}")
print(f"Minuti: {minutes}")
print(f"Secondi: {seconds}")

