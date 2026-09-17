import time
import network
from machine import Pin
from umqtt.simple import MQTTClient

# Red Wi-Fi y servidor
WIFI_SSID = "TU_RED_WIFI"
WIFI_PASS = "TU_CONTRASEÑA"
MQTT_SERVER = "IP_DE_TU_SERVIDOR"  # IP del servidor Mosquitto
CLIENT_ID = "NodeMCU_ESP8266_Python"

# Tópicos MQTT según la práctica
TOPICO_CONTROL = b"esp32/led/control"
TOPICO_ESTADO = b"esp32/led/estado"

# GPIO2 corresponde al pin D4 de la NodeMCU
led = Pin(2, Pin.OUT)
led.value(0)  # Estado inicial: apagado

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectándose a Wi-Fi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(1)
    print("Conexión Wi-Fi lista. IP:", wlan.ifconfig()[0])

def callback_mqtt(topic, msg):
    """Procesa los mensajes entrantes del servidor MQTT."""
    print(f"Mensaje recibido en [{topic.decode()}]: {msg.decode()}")
    
    if topic == TOPICO_CONTROL:
        if msg == b"on":
            led.value(1)
            client.publish(TOPICO_ESTADO, b"LED encendido", retain=True)
            print("Estado: LED Encendido")
        elif msg == b"off":
            led.value(0)
            client.publish(TOPICO_ESTADO, b"LED apagado", retain=True)
            print("Estado: LED Apagado")

# 1. Conexión a la red local
conectar_wifi()

# 2. Configuración y conexión del cliente MQTT
client = MQTTClient(CLIENT_ID, MQTT_SERVER)
client.set_callback(callback_mqtt)

try:
    client.connect()
    client.subscribe(TOPICO_CONTROL)
    print("Conectado al servidor MQTT. Escuchando en:", TOPICO_CONTROL.decode())
except Exception as e:
    print("Error al conectar con el servidor MQTT:", e)

# 3. Bucle infinito para recibir comandos
while True:
    try:
        client.check_msg()  # Escucha activa de mensajes entrantes
        time.sleep(0.1)
    except OSError as e:
        print("Reconectando a MQTT...")
        time.sleep(5)
        client.connect()
        client.subscribe(TOPICO_CONTROL)