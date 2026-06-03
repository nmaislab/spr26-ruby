# Read Pulse - Hardware Integration Script

## Overview

`read_pulse.py` is a Python script that reads pulse/ECG sensor data from hardware via SPI (Serial Peripheral Interface) and publishes the measurements to an MQTT broker for real-time monitoring and data collection.

## Purpose

- Interface with analog pulse/ECG sensors via SPI connection
- Real-time acquisition of biometric data from microcontroller
- Stream sensor data to MQTT broker for distributed processing
- Enable IoT integration for remote monitoring applications
- Support live ECG data visualization and analysis

## Hardware Requirements

### Microcontroller/SPI Master
- Raspberry Pi (recommended) or similar SBC with SPI support
- Python spidev library compatible
- GPIO pins available for SPI communication

### Sensor
- Analog pulse/ECG sensor (e.g., MAX30100, PPG sensor)
- ADC (Analog-to-Digital Converter) via MCP3008 or similar
- SPI interface or SPI-connected ADC

### Wiring
```
RPi GPIO    ← MCP3008/ADC    ← Pulse Sensor
CE0         → Chip Select
CLK         → Clock
MOSI        → Data In
MISO        → Data Out
GND         → Ground
3.3V        → Power

MCP3008 CH0 → Pulse Sensor Output
```

## Software Requirements

### Python Packages
```
spidev>=3.5         # SPI interface
paho-mqtt>=1.6.0    # MQTT client
```

### Installation

```bash
pip install spidev paho-mqtt
```

Or with requirements file:
```bash
pip install -r requirements.txt
```

### MQTT Broker
- Mosquitto (recommended)
- Local or remote broker instance
- Default: `localhost:1883`

## Script Overview

### Component 1: MQTT Client Setup
```python
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
```
- Creates MQTT client instance
- Connects to local broker on default port
- 60-second keep-alive timeout

### Component 2: SPI Interface
```python
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, Device 0
```
- Initializes SPI communication
- Opens /dev/spidev0.0 device
- Enables hardware data transfer

### Component 3: ADC Reading Function
```python
def read_adc(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    return ((adc[1]&3) << 8) + adc[2]
```
- Reads 10-bit value from specified ADC channel
- Communicates with MCP3008 ADC IC
- Returns digital value (0-1023)

**How it works**:
- Sends 3-byte SPI message: `[1, (8+channel)<<4, 0]`
- Receives 3-byte response with ADC value
- Extracts lower 10 bits from response bytes
- Combines high 2 bits (from adc[1]) with 8 bits (from adc[2])

### Component 4: Data Acquisition Loop
```python
while True:
    value = read_adc(0)      # Read from ADC channel 0
    print(value)             # Display to console
    client.publish("pulse/data", value)  # Publish to MQTT
    time.sleep(0.1)          # 100ms delay (10 Hz sampling)
```
- Continuous data collection
- Real-time console output
- MQTT publishing
- 10 Hz sampling rate (0.1s interval)

## Configuration

### MQTT Broker Settings
```python
client.connect("localhost", 1883, 60)
```
Modify as needed:
- **Host**: IP address or hostname of MQTT broker
- **Port**: Default 1883 (or 8883 for TLS)
- **Keepalive**: Seconds between keep-alive pings

### MQTT Topic
```python
client.publish("pulse/data", value)
```
Current topic: `pulse/data`

Customize topic hierarchy as desired:
- `sensors/pulse/raw`
- `ecg/channel0`
- `patient/001/pulse`

### SPI Configuration
```python
spi.open(0, 0)
```
- **Bus**: 0 (SPI0 on Raspberry Pi)
- **Device**: 0 (CE0 chip select)
- Modify if using different bus/device

### ADC Channel
```python
value = read_adc(0)
```
- Currently reading channel 0 of MCP3008
- Change argument to read different channels (0-7)

### Sampling Rate
```python
time.sleep(0.1)
```
- Current: 100ms interval = 10 Hz sampling
- Modify for different rates:
  - 0.05 → 20 Hz
  - 0.1 → 10 Hz
  - 0.2 → 5 Hz
  - 1.0 → 1 Hz

## Usage

### Basic Execution
```bash
python read_pulse.py
```

### With Output Redirection
```bash
python read_pulse.py > pulse_output.log 2>&1
```

### Background Execution
```bash
nohup python read_pulse.py &
```

### With Systemd Service
Create `/etc/systemd/system/pulse-reader.service`:
```ini
[Unit]
Description=Pulse/ECG Data Reader
After=network.target mosquitto.service

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/pulse_reader
ExecStart=/usr/bin/python3 /home/pi/pulse_reader/read_pulse.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable pulse-reader
sudo systemctl start pulse-reader
sudo systemctl status pulse-reader
```

## Data Format

### ADC Values
- **Range**: 0-1023 (10-bit)
- **Voltage Mapping**: value × (3.3V / 1023)
- **Raw Output**: Integer ADC counts

### MQTT Message
- **Topic**: `pulse/data`
- **Payload**: Integer value (0-1023)
- **QoS**: 0 (default, fire-and-forget)
- **Frequency**: 10 Hz (every 100ms)

### Example Values
```
523    # Mid-range reading
412    # Diastole (lower pressure)
678    # Systole (higher pressure)
```

## Monitoring & Debugging

### View MQTT Messages
```bash
mosquitto_sub -h localhost -t "pulse/data"
```

### Monitor with timeout
```bash
timeout 30 mosquitto_sub -h localhost -t "pulse/data"
```

### Check SPI Interface
```bash
ls -la /dev/spidev*
```

### Verify MQTT Broker
```bash
mosquitto -v  # Run broker with verbose output
# or
sudo systemctl status mosquitto
```

### Test ADC Directly
```bash
python3 -c "
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)
adc = spi.xfer2([1, 8<<4, 0])
print('ADC value:', ((adc[1]&3) << 8) + adc[2])
spi.close()
"
```

## Troubleshooting

### Error: "Cannot access /dev/spidev0.0"
**Cause**: SPI not enabled or permission denied
**Solutions**:
```bash
# Enable SPI on Raspberry Pi
sudo raspi-config  # Interface Options → SPI
# Or run with sudo
sudo python read_pulse.py
```

### Error: "Connection refused" (MQTT)
**Cause**: MQTT broker not running or incorrect address
**Solutions**:
```bash
# Check broker status
sudo systemctl status mosquitto
# Start broker if needed
sudo systemctl start mosquitto
# Verify connectivity
mosquitto_pub -h localhost -t "test" -m "hello"
```

### Values always 0 or always 1023
**Cause**: Sensor not connected, ADC misconfigured, or wrong channel
**Solutions**:
- Check SPI wiring
- Verify ADC channel number
- Test with different channels
- Check sensor power and connections

### High noise in readings
**Cause**: Electromagnetic interference, loose connections, or ground loops
**Solutions**:
- Shield SPI cables
- Use shorter wires
- Add capacitive filter to analog input
- Ensure proper grounding
- Implement software averaging

### Slow/Intermittent Data
**Cause**: MQTT broker overloaded, slow network, or SPI issues
**Solutions**:
- Reduce sampling frequency (increase sleep time)
- Check network connectivity
- Monitor CPU usage
- Check SPI clock speed

## Integration with Analysis

### Connect to Jupyter Notebook
Use MQTT client library to subscribe to topic:
```python
import paho.mqtt.client as mqtt
import numpy as np

data_buffer = []

def on_message(client, userdata, msg):
    value = int(msg.payload.decode())
    data_buffer.append(value)

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("pulse/data")
client.loop_start()
```

### Real-time Visualization
Stream to plotting framework:
```bash
# Using tools like Grafana with InfluxDB backend
# or custom WebSocket visualization
```

## Performance Considerations

### Sampling Rate
- 10 Hz (current): Adequate for ECG with 360 Hz data
- Limitation: SPI bandwidth on RPi ~6 Mbps
- Maximum theoretical: ~1000 Hz with optimization

### Latency
- SPI communication: ~1ms
- MQTT publishing: ~10-50ms
- Total: ~50-100ms typical

### Power Consumption
- Raspberry Pi: ~2-3W
- MCP3008 ADC: <5mW
- Total system: 2-5W depending on connected sensors

## Security Considerations

### MQTT Security
Current implementation has no authentication:
```python
client = mqtt.Client()  # Unsecured
```

For production, use:
```python
client.username_pw_set("username", "password")
client.tls_set(ca_certs="ca.crt")
client.connect("broker.example.com", 8883)  # TLS port
```

### SPI Security
- SPI is local only (typically on RPi)
- No special security needed for local sensors

## Advanced Usage

### Multi-channel Reading
```python
while True:
    for channel in range(8):
        value = read_adc(channel)
        client.publish(f"pulse/channel{channel}", value)
    time.sleep(0.1)
```

### Data Logging to File
```python
with open('pulse_data.csv', 'a') as f:
    while True:
        value = read_adc(0)
        timestamp = time.time()
        f.write(f"{timestamp},{value}\n")
        client.publish("pulse/data", value)
        time.sleep(0.1)
```

### Conditional Publishing
```python
while True:
    value = read_adc(0)
    if value > 500:  # Only publish high values
        client.publish("pulse/data", value)
    time.sleep(0.1)
```

## Related Files

- `MIT_BIH_Arrythmia.ipynb` - Offline ECG analysis notebook
- `README.md` - Main project documentation

## References

- [SPIDEV Documentation](https://pypi.org/project/spidev/)
- [Paho MQTT Python](https://pypi.org/project/paho-mqtt/)
- [MCP3008 Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/21295d.pdf)
- [Raspberry Pi SPI Setup](https://www.raspberrypi.org/documentation/computers/config_txt.html)
- [MQTT Protocol](https://mqtt.org/)

---

**Version**: 1.0  
**Status**: Production-ready  
**Last Updated**: Current research phase
