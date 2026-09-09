import paho.mqtt.client as mqtt
import sys

# Variable global para el tópico
topico = ""

# Funcion invocada cuando se establece la conexion con el servidor MQTT
def on_connect(cliente, userdata, flags, rc, properties=None):
    global topico
    print(f"Conectado con el codigo {rc}")
    # El cliente se subscribe al topico en el servidor MQTT
    cliente.subscribe(topico)

# Funcion invocada cuando se recibe un mensaje del servidor MQTT 
def on_message(cliente, userdata, message):
    print(f"Topico: {message.topic}, Mensaje: {message.payload.decode()}")

# Comprueba que se reciben el numero esperado de parametros en la linea de comandos
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Error. Uso: python paho_sub.py [urlServidor] topico")
    sys.exit(-1)

# En el caso que se omita la direccion IP del servidor MQTT -> Servidor MQTT local
if len(sys.argv) == 2:
    urlServidor = "localhost"
    topico = sys.argv[1]
# En el caso de que el servidor MQTT sea remoto
else:
    urlServidor = sys.argv[1]
    topico = sys.argv[2]

# Crea una instancia de la clase Client
cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

cliente.on_connect = on_connect
cliente.on_message = on_message

# Establece una conexion con el servidor MQTT
cliente.connect(urlServidor)

# Se mantiene en un ciclo de espera de los mensajes del servidor
cliente.loop_forever()