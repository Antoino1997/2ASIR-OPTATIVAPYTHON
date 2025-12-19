import time

def tick_tock(seconds):
    for i in range(1, seconds + 1):
        if i % 2 != 0:
            print("Tick...")
        else:
            print("Tock...")

        time.sleep(1)

print("How much time do you want to wait?")
segundos = int(input())
tick_tock(segundos)