import pandas as pd
import matplotlib.pyplot as plt

# Filsti til CSV-filen
filnavn = "Målinger/fordobling.csv"  # <-- Endre til ditt filnavn

# Les data, hopp over de første 19 linjene (starter på linje 20)
df = pd.read_csv(filnavn, skiprows=19, encoding='latin1')

# Rens kolonnenavn
df.columns = [col.strip() for col in df.columns]

# Hent og konverter verdier
tid = pd.to_numeric(df['Time (s)'], errors='coerce')
kanal1 = pd.to_numeric(df['Channel 1 (V)'], errors='coerce')*30
kanal2 = pd.to_numeric(df['Channel 2 (V)'], errors='coerce')

# Fjern ugyldige rader
mask = tid.notna() & kanal1.notna() & kanal2.notna()
tid = tid[mask]
kanal1 = kanal1[mask]
kanal2 = kanal2[mask]

# Plot
plt.figure(figsize=(12, 6))
plt.plot(tid, kanal1, label='Utgang (V)', linewidth=1.5)
plt.plot(tid, kanal2, label='Inngang (V)', linewidth=1.5)
plt.xlabel('Tid [s]')
plt.ylabel('Spenning [V]')
plt.title('Tidssignaler for Kanal 1 og 2')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
