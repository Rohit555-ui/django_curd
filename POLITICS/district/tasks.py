# Create your tasks here

from celery import shared_task
import logging
#from .models import Widget


@shared_task
def add(x, y):
    logger = logging.getLogger(__name__)
    logger.error("error logging in except field!!!!")
    import time
    print("before sleep it is running")
    time.sleep(5)
    print("after sleep")
    # return x + y

@shared_task
def run_after_5(name):
    print("run after 5 seconds function is getting called", name)

@shared_task
def post_add(a, b):
    logger = logging.getLogger(__name__)
    logger.error("error logging in except field!!!!")
    import time
    print(a, b)
    print("before sleep function")
    time.sleep(5)
    print("after sleep function")

@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# @shared_task
# def count_widgets():
#     return Widget.objects.count()
#
#
# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()


# import schedule, time
#
# def job():
#     try:
#         a = 10/0
#         print("I'm working...")
#     except Exception as e:
#         print("exception raised")
#
# schedule.every(5).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)