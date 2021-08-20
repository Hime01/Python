from termcolor import colored
from time import sleep
from itertools import cycle


class TrafficLight:
    __color = [{'text': 'красный', 'color': 'red', 'secs': 7}, {'text': 'желтый', 'color': 'yellow', 'secs': 2},
               {'text': 'зеленый', 'color': 'green', 'secs': 7}]

    def running(self):
        count = 0
        for col in cycle(self.__color):
            if count > 20:
                break
            print(f'{colored(col["text"], col["color"])}')
            sleep(col["secs"])
            count += 1


my_trafficlight = TrafficLight()
my_trafficlight.running()
