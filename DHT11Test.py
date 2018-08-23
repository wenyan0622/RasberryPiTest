import Adafruit_DHT
sensor1=Adafruit_DHT.DHT11
humdity,temperature=Adafruit_DHT.read_retry(sensor1,4);
print("humdity:");
print(humdity);
print("temperature:");
print(temperature);
