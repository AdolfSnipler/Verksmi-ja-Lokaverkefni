from machine import Pin
from myservo import myServo
from time import sleep_ms
from umqtt.simple import MQTTClient
import asyncio

led1 = 4
led2 = 5
led_pin1 = Pin(led1, Pin.OUT)
led_pin2 = Pin(led2, Pin.OUT)

servo = myServo(9) # Pininn sem servo-inn er tengdur við
servo_hendi_R= myServo(8) #Pininn sem servo fyrir háls er tengdur við
servo_hendi_L= myServo(7)
teljari = 0

# ------------ Tengjast WIFI -------------
WIFI_SSID = "T Skoli Hotspot"
WIFI_LYKILORD = ""

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_LYKILORD)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
do_connect()

# ---------------- MQTT ------------------

MQTT_BROKER = "test.mosquitto.org"
CLIENT_ID = "Sendir"
TOPIC = b"2481kynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna

servo.myServoWriteAngle(170)
servo_hendi_R.myServoWriteAngle(90) #180 er uppi á right
servo_hendi_L.myServoWriteAngle(90) #0 er uppi á left
fekk_skilabod_virkni = 1
led_pin2.value(0)
led_pin1.value(0)

async def senda_skilabod():
    global senda_nuna
    print("starta senda_skilabod")
    while True:
        
        if senda_nuna == True:
            print("senda_skilabod")
            skilabod = "Move mouth!"
            mqtt_client.publish(TOPIC, skilabod)
            senda_nuna = False
        await asyncio.sleep_ms(0)    



def fekk_skilabod(topic, skilabod):
    global fekk_skilabod_virkni
    print("fekk_skilabod")
    print(f"TOPIC: {topic.decode()}, skilaboð: {skilabod}")
    fekk_skilabod_virkni = 0
    return skilabod

mqtt_client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
mqtt_client.set_callback(fekk_skilabod)
mqtt_client.connect()
mqtt_client.subscribe(b"2480kynning")

senda_nuna = True

async def mottaka_skilabod():
    while True:
        mqtt_client.check_msg()
        await asyncio.sleep_ms(0)
    print("mottaka")

async def hreyfing():
    print("starta hreyfing")
    teljari = 87
    global fekk_skilabod_virkni, senda_nuna
    while True:
        if fekk_skilabod_virkni == 0:
            led_pin2.value(1)
            led_pin1.value(1)
            servo.myServoWriteAngle(teljari)
            servo_hendi_R.myServoWriteAngle(180)
            servo_hendi_L.myServoWriteAngle(0)
            await asyncio.sleep(3)
            teljari = teljari + 83
            servo_hendi_R.myServoWriteAngle(90)
            servo_hendi_L.myServoWriteAngle(90)
            servo.myServoWriteAngle(teljari)
            led_pin2.value(0)
            led_pin1.value(0)
            print("hreyfing")
            fekk_skilabod_virkni = 2
            senda_nuna = True
        await asyncio.sleep_ms(0)
        
# In each ESP module, replace while True loop and main definition with:

async def main():
    global senda_nuna
    while True:
        await asyncio.gather(mottaka_skilabod(), hreyfing(), senda_skilabod())
    await asyncio.create_task(senda_skilabod())
    await asyncio.sleep(0.1)  # allows some delay for other tasks
    while True:
        await asyncio.sleep(3)  # allows some delay for other tasks
        senda_nuna = False
if __name__ == "__main__":
    asyncio.run(main())





