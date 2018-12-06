import numpy as np
from scipy.signal import butter
import mne
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    #montage = mne.channels.read_montage('standard_1020')
    #print(montage.ch_names)

    # Initialising Parameters
    raw = mne.io.read_raw_edf('../dataset/BCICIV_2b_gdf/B0101T.gdf', preload=True)
    data = raw.get_data()
    #montage = mne.channels.read_montage("standard_1020")
    events = mne.find_events(raw, initial_event=True)
    print(events)
    
    # Setting Parameters
    #raw.set_montage(montage)
    #raw.set_eeg_reference("average")
    
    # Show plot
    #plt.plot(raw.get_data[-1])
    raw.plot(block=True, events=events)
