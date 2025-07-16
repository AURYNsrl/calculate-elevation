import math

def calcola_elevazione(distanza):
    """
    Calcola l'elevazione minima e massima che un aereo può raggiungere rispetto a un punto dato,
    considerando un angolo minimo di 7° e massimo di 37°.
    
    :param distanza: Distanza orizzontale dal punto di riferimento (in metri)
    :return: (elevazione_min, elevazione_max) in metri
    """
    angolo_min = math.radians(7)  # Converti in radianti
    angolo_max = math.radians(37)
    
    elevazione_min = math.tan(angolo_min) * distanza
    elevazione_max = math.tan(angolo_max) * distanza
    
    return elevazione_min, elevazione_max

# Esempio di utilizzo
distanza = float(input("Inserisci la distanza dal punto di riferimento (in metri): "))
elev_min, elev_max = calcola_elevazione(distanza)
print(f"Elevazione minima: {elev_min:.2f} m")
print(f"Elevazione massima: {elev_max:.2f} m")
