import numpy as np
from scipy.io.wavfile import write

#samples per sec
sps = 44100

freq_hz = 440.0

duration_s = 5.0 

each_sample_number = np.arange(duration_s * sps)
waveform = np.sin(2 * each_sample_number * freq_hz / sps)
waveform_quiet = waveform * 0.3
waveform_intergers = np.int16(waveform_quiet * 32767)
write('first_sine_wave.wav', sps, waveform_intergers)
