# import subprocess
# import sounddevice as sd
# import numpy as np
# import pandas as pd
# import json

# input_device_id = 2
# duration = 0.5  # Duration of each audio sample in seconds
# samplerate = 48000  # Sample rate (samples per second)
# current_amplitude = []
# datacollected = []
# current_data_input = []

# def callback(indata, frames, time, status):
#     # Calculate the average amplitude value
#     average_amplitude = np.mean(np.abs(indata))
#     # print(f"Average Amplitude Value: {average_amplitude:.6f}")
#     if len(current_amplitude) >= 4:
#         myseries = pd.Series(current_amplitude)
#         datacollected.append(myseries)
#         del current_amplitude[0]
#     current_amplitude.append(average_amplitude)
#     print(current_amplitude)



# # Start streaming audio input
# with sd.InputStream(samplerate=samplerate, channels=1, callback=callback, blocksize=int(samplerate * duration)):
#     try:
#         print("Average Amplitude Values (Press Ctrl+C to stop)")
#         while True:
#             output = subprocess.check_output(["osascript", "-e", "output volume of (get volume settings)"])
#             current_volume = int(output.strip())
#             print(f"Current Volume Level: {current_volume}")
            
#             pass
#     except KeyboardInterrupt:
#         datacollected = pd.DataFrame(datacollected)
#         datacollected.to_csv('./test_csv.csv')
#         print("\nStopped by user")
from Controllers.encrypter import AEA

decoder = AEA(key_path='./PvtInfo/important_key.json')
github = decoder.decrypt_file('./PvtInfo/github_token.txt')
google= decoder.decrypt_file('./PvtInfo/google_token.txt')
print(github)
print(google)