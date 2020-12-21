import comms
import time

if __name__ == '__main__':
    comms.pins_only(["green"]) #Opening Forest is green
    time.sleep(4.36)
    comms.pins_only(["green", "blue"]) # Turqoise Ocean 4:22
    time.sleep(5.52) # 5:31
    comms.pins_only(["blue"]) # Blue Spaceship 9:53
    time.sleep(6.2) # 6:12
    comms.pins_only(["red"]) # Red Nether 16:05
    time.sleep(4.66) # 4:40
    comms.pins_only(["red", "blue"]) # Purple Movent 20:45
    #time.sleep()
    #comms.pins_only([]) # Purple Spaceship
    time.sleep(7.17) # 7:10
    comms.pins_only(["wwhite"]) # White Sun 27:55
    time.sleep(2.75) # 2:45
    comms.pins_only([]) # End 30:50
