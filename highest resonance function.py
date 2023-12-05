import os
import tkinter as tk
from tkinter import filedialog
from scipy.io import wavfile
import numpy as np
from pydub import AudioSegment

import os
from scipy.io import wavfile
import numpy as np

def compute_highest_resonance_frequency(file_path='16bit1chan.wav', default_frequency=440.0):
    try:
        sample_rate, data = wavfile.read(file_path)
        highest_amplitude_index = np.argmax(np.abs(np.fft.fft(data)))
        highest_resonance_frequency = highest_amplitude_index * sample_rate / len(data)
        print(f"Highest Resonance Frequency: {highest_resonance_frequency:.2f} Hz")
        return highest_resonance_frequency

    except Exception as e:
        print(f"Error: {e}")
        print(f"Using default frequency: {default_frequency} Hz")
        return default_frequency

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, '16bit1chan.wav')
compute_highest_resonance_frequency(file_path)
