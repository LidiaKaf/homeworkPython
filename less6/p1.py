import time


class TrafficLight:
    __color = 'красный'

    def running(self):
        __color = 'красный'
        print(__color)
        time.sleep(7)
        __color = 'желтый'
        print(__color)
        time.sleep(2)
        __color = 'зеленый'
        print(__color)
        time.sleep(5)



t = TrafficLight()
t.running()



