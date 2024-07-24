# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES 

import sounddevice as sd
import numpy as np
import wave
import time

# --------------------------------------------------------------------------------------------------------

def record_audio(duration, filename):
    # Sampling frequency
    fs = 44100  # 44100 samples per second

    print("Recording started...")
    # Record audio for the given duration
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")

    # Save the audio data to a WAV file
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(2)  # Stereo
        wf.setsampwidth(2)  # 2 bytes per sample
        wf.setframerate(fs)
        wf.writeframes(audio_data.tobytes())
    print(f"Audio saved to {filename}")



# Record audio for 30 seconds when the microphone gets activated
# listen_and_record(duration=15)