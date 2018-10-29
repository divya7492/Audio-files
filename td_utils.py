import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
from pydub import AudioSegment

# Calculate and plot spectrogram for a wav audio file
def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    nfft = 200 # Length of each window segment
    fs = 8000 # Sampling frequencies
    noverlap = 120 # Overlap between windows
    nchannels = data.ndim
    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap = noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:,0], nfft, fs, noverlap = noverlap)
    return pxx

# Load a wav file
def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data

# Used to standardize volume of audio clip
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Load raw audio files for speech synthesis
def load_raw_audio():
    positive= []
    backgrounds = []
    negative = []
    for filename in os.listdir("./new/positive"):
        if filename.endswith("wav"):
            help = AudioSegment.from_wav("./new/positive/"+filename)
            positive.append(help)
    for filename in os.listdir("./new/background"):
        if filename.endswith("wav"):
            help_background = AudioSegment.from_wav("./raw_data/background/"+filename)
            background.append(help_background)
    for filename in os.listdir("./raw_data/negative"):
        if filename.endswith("wav"):
            help_negative = AudioSegment.from_wav("./raw_data/negative/"+filename)
            negative.append(help_negative)
    return help, help_negative, help_background