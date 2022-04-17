# Sound recording for mcp3208/mcp3008 with raspberrypi
- It is not recommend sound recording use mcp3208/mcp3008
- Just want you to know that it's possible


## require library
---
- spidev
```
pip install spidev
```

## raspi config
---
- set SPI enable in raspi-config
- set dtparam=spi=on, dtoverlay=spi(spi_pin_num)-(cs_pin_num)cs in /boot/config.txt
- ex) if mcp3208 connect spi pin 1, cs pin 1 => dtoverlay=spi1-1cs

## info
---
- Only framerate over 20000 correct sync
- but framerate over 20000 makes many recording noise