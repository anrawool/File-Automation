import pyaudio
import numpy as np

# Initialize PyAudio and audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024
)

try:
    while True:
        # Read audio data from the stream
        data = stream.read(1024)
        # Convert the binary audio data to a NumPy array
        audio_signal = np.frombuffer(data, dtype=np.int16)
        # Calculate the root mean square (RMS) of the audio signal
        rms = np.sqrt(np.mean(np.square(audio_signal)))
        # Convert RMS to decibels (dB)
        db = 20 * np.log10(rms)

        print(f"Decibel level: {db:.2f} dB")

except KeyboardInterrupt:
    pass

# Close the audio stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()

