from myservo import myServo
import time
from machine import Pin, PWM
import asyncio

led1 = 4
led2 = 5
led_pin1 = Pin(led1, Pin.OUT)
led_pin2 = Pin(led2, Pin.OUT)

servo = myServo(9) # Pininn sem servo-inn er tengdur við
servo_hals = myServo(8) #Pininn sem servo fyrir háls er tengdur við
teljari = 0
from machine import Pin
from time import sleep_ms
from umqtt.simple import MQTTClient

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
CLIENT_ID = "Mottakari"
TOPIC = b"2480kynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna

servo.myServoWriteAngle(170)
servo_hals.myServoWriteAngle(90)
fekk_skilabod_virkni = 0
led_pin2.value(0)
led_pin1.value(0)
senda_nuna = True

# Callback fall, keyrir þegar skilaboð berast með MQTT
def fekk_skilabod(topic, skilabod):
    global fekk_skilabod_virkni
    print("skilaboð ready")
    print(f"TOPIC: {topic.decode()}, skilaboð: {skilabod}")
    fekk_skilabod_virkni = 0
    return
    # ATH. skilaboðin berast sem strengur

mqtt_client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
mqtt_client.set_callback(fekk_skilabod) # callback fallið skilgreint
mqtt_client.connect()
mqtt_client.subscribe(b"2481kynning")


async def mottaka_skilabod():
    print("tf")
    while True:
        mqtt_client.check_msg()
        await asyncio.sleep(0)

    
async def hreyfing():
    global fekk_skilabod_virkni
    print("we are in boys")
    if fekk_skilabod_virkni == 0:
        await asyncio.sleep(5)
        teljari = 87
        led_pin2.value(1)
        led_pin1.value(1)
        servo.myServoWriteAngle(teljari)
        await asyncio.sleep(1)
        for angle in range(90, 45, -1):  # from 45 to -45
            servo_hals.myServoWriteAngle(angle)
            await asyncio.sleep_ms(10)
        for angle in range(45, 135):  # from 45 to -45
            servo_hals.myServoWriteAngle(angle)
            await asyncio.sleep_ms(10)
        for angle in range(135, 90, -1):  # from 45 to -45
            servo_hals.myServoWriteAngle(angle)
            await asyncio.sleep_ms(10)
        teljari = teljari + 83
        servo.myServoWriteAngle(teljari)
        await asyncio.sleep(1)
        led_pin2.value(0)
        led_pin1.value(0)
        print("hreyfing")
        fekk_skilabod_virkni = 0
        return
    
            
async def senda_skilabod():
    while True:
        if senda_nuna == True:
            print("sending...")
            skilabod = "do something!"
            mqtt_client.publish(TOPIC, skilabod)
            await asyncio.sleep(10)

async def main():
    global senda_nuna
    while True:
        mqtt_client.check_msg()
        await asyncio.gather(mottaka_skilabod(), hreyfing(), senda_skilabod())
        await asyncio.create_task(senda_skilabod())
    await asyncio.sleep(0.1)  # allows some delay for other tasks
    while True:
        await asyncio.sleep(3)  # allows some delay for other tasks
        senda_nuna = False

# At the bottom of your script, outside any function:
if __name__ == "__main__":
    asyncio.run(main())





