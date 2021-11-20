import time


class TrafficLight:
    _colors = ['красный', 'желтый', 'зеленый']


    def running(self):
        timer = 0
        while timer != 6:
            for i in TrafficLight._colors:
                timer += 1
                print(i)
                if i == 'желтый':
                    time.sleep(2)
                else:
                    time.sleep(7)


TrafficLight = TrafficLight()
TrafficLight.running()


