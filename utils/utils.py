from datetime import datetime


def now():
    return datetime.now().strftime("-%d-%m-%Y-%H-%M-%S")
