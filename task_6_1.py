from time import sleep

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 1
        while True:
            if i % 2 == 0:
                print(f'{TrafficLight.__color[1]}')
                sleep(2)
            elif i % 3 == 0:
                print(f'{TrafficLight.__color[2]}')
                sleep(7)
            else:
                print(f'{TrafficLight.__color[0]}')
                sleep(7)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

