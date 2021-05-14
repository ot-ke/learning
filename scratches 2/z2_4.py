# Написать мультипоточную программу. #
# B основном потоке программа печатает сообщение "main" в параллельном потоке функция печатает сообщение "thread"
# Программа работает 10 секунд.

import time
import threading
from threading import Thread
from time import sleep

def cycle_thread(name):
    start_time = time.time()
    while True:
        if time.time() - start_time > 2:
            break
        print("klassny ", name)
        sleep(0.5)



thread1 = Thread(target=cycle_thread, args=("Yuryj ",))
thread2 = Thread(target=cycle_thread, args=("ne Yuryj ",))


thread1.start()
thread2.start()

start_time = time.time()
while True:
    if time.time() - start_time > 1:
        break
    print("ne klassny ")
    sleep(0.3)


thread1.join()
thread2.join()

print("end")


