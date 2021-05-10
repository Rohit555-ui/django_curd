import schedule
import time

def geeks():
    print("geeks function is getting called!!!")

print("rohit")





schedule.every(2).seconds.do(geeks)

# while True:
schedule.run_pending()
schedule.run_pending()
