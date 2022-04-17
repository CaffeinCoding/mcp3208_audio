import spidev, time

spi = spidev.SpiDev()
spi.open(1,2) # raspi pin number connect mcp3208
spi.max_speed_hz = 2000000

class mcp3208mic():
    def __init__(self, frames_per_buffer):
        self._frame_per_buffer = frames_per_buffer
        self._checkAudio = True
        self._audioBuf = []
        self._channel = 1 # mic/sound sensor number
        
    def close(self):
        self._checkAudio = False
        return
    
    def record(self, timedata):
        set_t = time.time() + timedata
        while time.time() < set_t:
            audio_data = self.analogRead(self._channel)
            self._audioBuf.append(audio_data.to_bytes(2, 'big'))
        return b''.join(self._audioBuf)
    
    def analogRead(self, channel):
        r = spi.xfer2([1,(8+channel) << 4,0])
        adc_out = ((r[1]&3) << 8) + r[2]
        return adc_out