import wave
import mcp3208record

rate = 21000
chunk = 4096 # mcp3208 bit(12bit) / mcp3008 bit(10bit)
record_seconds = 5
channel = 1
wave_filename = 'file.wav'

mic = mcp3208record.mcp3208mic(chunk)

frames = mic.record(record_seconds)
print('record done')

wavefile = wave.open(wave_filename, 'wb')
wavefile.setnchannels(channel)
wavefile.setsampwidth(2) # analog data size of 1bit
wavefile.setframerate(rate)
wavefile.writeframes(frames)
wavefile.close()