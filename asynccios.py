from machine import Pin, PWM, ADC
from myservo import myServo
import uasyncio as asyncio

ai1 = Pin(12, Pin.OUT)
ai2 = Pin(13, Pin.OUT)
pwmA = PWM(Pin(14, Pin.OUT), 10000)

servo = myServo(9)

potentiometer = ADC(Pin(7))
potentiometer.atten(ADC.ATTN_11DB)

async def afram(hradi, ai1, ai2, pwmA):
    ai1.value(1)
    ai2.value(0)
    pwmA.duty(hradi)

async def aftur(hradi, ai1, ai2, pwmA):
    ai1.value(0)
    ai2.value(1)
    pwmA.duty(hradi)

async def stopp(ai1, ai2, pwmA):
    ai1.value(0)
    ai2.value(0)
    pwmA.duty(0)

async def control_servo(servo):
    
    while True:
        for angle in range(0, 181):
            pot_value = potentiometer.read() // 205
            servo.myServoWriteAngle(angle)
            await asyncio.sleep_ms(pot_value)

        for angle in range(180, -1, -1):
            pot_value = potentiometer.read() // 205
            servo.myServoWriteAngle(angle)
            await asyncio.sleep_ms(pot_value)

async def main():
    asyncio.create_task(control_servo(servo))

    while True:
        await afram(200, ai1, ai2, pwmA)
        await asyncio.sleep_ms(1000)
        await stopp(ai1, ai2, pwmA)
        await asyncio.sleep_ms(100)
        await aftur(200, ai1, ai2, pwmA)
        await asyncio.sleep_ms(1000)
        await stopp(ai1, ai2, pwmA)
        await asyncio.sleep_ms(100)
        
        await asyncio.sleep_ms(0) 

asyncio.run(main())
