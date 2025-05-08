import pandas as pd
import numpy as np

def finn_periode(data):
    tid = data['Time (s)'].values
    verdi = data['Channel 1 (V)'].values

    # Finn alle stigende nullkryss (fra negativ til positiv)
    nullkryss = []
    for i in range(1, len(verdi)):
        if verdi[i - 1] < 0 and verdi[i] >= 0:
            # Lineær interpolasjon for mer presist nullpunkt
            t0, t1 = tid[i - 1], tid[i]
            v0, v1 = verdi[i - 1], verdi[i]
            t_null = t0 - v0 * (t1 - t0) / (v1 - v0)
            nullkryss.append((i, t_null))

    if len(nullkryss) < 2:
        raise ValueError("Fant ikke minst to stigende nullkryss for å definere én periode.")

    # Indekser mellom første og andre nullkryss utgjør én periode
    start_idx = nullkryss[0][0]
    end_idx = nullkryss[1][0]

    return data.iloc[start_idx:end_idx+1]

def behandle_csv(input_fil, output_fil):
    data = pd.read_csv(input_fil, skiprows=19,encoding='latin1')

    # Behold kun relevante kolonner
    data = data[['Time (s)', 'Channel 1 (V)']]

    periode_data = finn_periode(data)
    periode_data.to_csv(output_fil, index=False)
    print(f"Ny CSV-fil med én periode skrevet til: {output_fil}")


if __name__ == "__main__":
    behandle_csv("Målinger/fordobling.csv", "en_periode_signal.csv")
