import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def onsket_signal(t,phi):
    return np.sin(2*np.pi*5800*t + phi)

def plott_signal(filsti):
    # Les CSV-data
    data = pd.read_csv(filsti, encoding='latin1')
    

    # Pass på at nødvendige kolonner finnes
    if 'Time (s)' not in data.columns or 'Channel 1 (V)' not in data.columns:
        raise ValueError("CSV-filen må inneholde kolonnene 'Time (s)' og 'Channel 1 (V)'.")
    
    t = np.linspace(data['Time (s)'][0],data['Time (s)'][0]+1/5800,len(data['Time (s)']))
    data['Channel 1 (V)'] = data['Channel 1 (V)'] * (1/max(data['Channel 1 (V)']))

    py_integral = 0
    pd_integral = 0
    i = 0

    for t in data['Time (s)']:
        py_integral += onsket_signal(t,-data['Time (s)'][0]*2*np.pi*5800)**2
        pd_integral += data['Channel 1 (V)'][i]**2 - onsket_signal(t,-data['Time (s)'][0]*2*np.pi*5800)**2
        i += 1
   
    py_integral *= 1/(data['Time (s)'].iloc[-1]-data['Time (s)'][0])
    pd_integral *= 1/(data['Time (s)'].iloc[-1]-data['Time (s)'][0])

    sdr = py_integral/pd_integral

    print(sdr)
   
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(data['Time (s)'], data['Channel 1 (V)'], label='Channel 1 (V)')
    plt.plot(t, onsket_signal(t,-data['Time (s)'][0]*2*np.pi*5800), label='Ønsket signal')
    plt.title('Signal over tid')
    plt.xlabel('Tid (s)')
    plt.ylabel('Spenning (V)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plott_signal("en_periode_signal.csv")  
