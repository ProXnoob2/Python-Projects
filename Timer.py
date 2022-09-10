import time
def countdown(t) :
    while t>0:
        print(t)
        t=t-1
        time.sleep(1)
    print("Time's Up")

print("Set The Timer Please. Enter an Integer.")
seconds = input()
while not seconds.isdigit():
    print("That Was Not An Integer Number! Please Enter An Integer.")
    seconds = input()
seconds = int(seconds)
countdown(seconds)