import time
def countdown(n):
    print(n)
    if n > 0:
        time.sleep(1)
        countdown(n-1)

countdown(5)