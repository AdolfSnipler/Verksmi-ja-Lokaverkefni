from machine import Pin, ADC
import asyncio
from lib.dfplayer import DFPlayer

df = DFPlayer(1) 
df.init(tx=4, rx=5) # tx á esp tengist í rx á mp3


start_stop_takki = Pin(7, Pin.IN, Pin.PULL_UP)
er_ad_spila = Pin(21, Pin.IN, Pin.PULL_UP) # 0 mp3 er að spila, 1 mp3 er ekki að spila

a_ad_spila = False
stada_ss_takka_adur = 1

async def main():
    global a_ad_spila, stada_ss_takka_adur
    await df.wait_available() # bíðum eftir að spilarinn er tilbúinn
    while True:
        stada_ss_takka = start_stop_takki.value()
        if stada_ss_takka == 0 and stada_ss_takka_adur == 1:
            a_ad_spila = not a_ad_spila
        stada_ss_takka_adur = stada_ss_takka
        
        if a_ad_spila == True:
            if er_ad_spila.value() == 1:
                print("spila lag")
                await df.play(1,1) # spila lag 1 í möppu 1
        else:
            if er_ad_spila.value() == 0:
                await df.stop()
                

        await df.volume(5)
        await asyncio.sleep_ms(0) # þarf ekki í þessu tilfelli en má vera

asyncio.run(main())