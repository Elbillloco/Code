import paho.mqtt.client as mqtt
import sys

# Funcion invocada cuando se publica un mensaje al servidor MQTT 
def on_publish(client, userdata, mid, reason_code, properties=None):
    print("Se publicaron los datos\n")

# Comprueba que se reciben el numero esperado de parametros en la linea de comandos
if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Error. Uso: python paho_pub.py [urlServidor] topico mensaje")
    sys.exit(-1)

# En el caso que se omita la direccion IP del servidor MQTT -> Servidor MQTT local
if len(sys.argv) == 3:
    urlServidor = "localhost"
    topico = sys.argv[1]
    mensaje = sys.argv[2]
# En el caso de que el servidor MQTT sea remoto
else:
    urlServidor = sys.argv[1]
    topico = sys.argv[2]
    mensaje = sys.argv[3]

# Crea una instancia de la clase Client
cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Se registra la funcion callback
cliente.on_publish = on_publish

# Establece una conexion con el servidor MQTT
cliente.connect(urlServidor)

# Publica un mensaje a un topico
cliente.publish(topic=topico, payload=mensaje)