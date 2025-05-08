import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

# Filsti til CSV-filen
filnavn = "Målinger/fordoblingSpectrum.csv"  # <-- Endre til riktig filnavn

# Les data, hopp over de første 6 linjene (startlinje = 7)
df = pd.read_csv(filnavn, skiprows=5)

# Rens kolonnenavn
df.columns = [col.strip() for col in df.columns]

# Hent og konverter frekvens og RMS
frekvens = pd.to_numeric(df['Frequency (Hz)'], errors='coerce')
rms = pd.to_numeric(df['Trace 1 (?)'], errors='coerce')

# Fjern ugyldige eller nullverdier
mask = (frekvens > 0) & (rms > 0)
frekvens = frekvens[mask]
rms = rms[mask]

# Sett alle verdier under terskel til null
terskel = 1e-4  # Juster etter behov
rms[rms < terskel] = 0

# Plot
plt.figure(figsize=(12, 6))
plt.plot(frekvens, rms, linewidth=1)
plt.xscale('log')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('RMS [V]')
plt.title('Spektrumanalyse – Frekvens vs RMS (filtrert)')
plt.grid(True, which='both', ls=':')

# Flere x-ticks på log-aksen
ax = plt.gca()
ax.xaxis.set_major_locator(LogLocator(base=10.0, numticks=15))
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=100))
ax.xaxis.set_minor_formatter(plt.NullFormatter())

# Sett y-aksegrense
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
