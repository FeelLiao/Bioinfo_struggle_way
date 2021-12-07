import time
from conf import settings
def logger(msg):
    with open(settings.LOG_PATH, mode="at", encoding="utf-8") as f:
        f.write("{} {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),msg))