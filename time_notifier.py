from datetime import datetime
import winsound
import typing
import time

# CONFIGURATIONS
MINUTES_TO_TRACK = [0, 15, 30, 45]
TIME_READ_SPEED = 1
NOTIFICATION_SOUND_PATH = "./notification.wav"

#
# A Butterfly effect speculation:
#  
# Not all things grow bigger inevitably,
# You can also de-escalate things,
# Little by little,
# You can do this with bad habits.
#

def get_minute() -> int:
    return datetime.now().minute

def get_full_date() -> str:
    return datetime.now().strftime("%m/%d/%Y %H:%M:%S ms: %f")

def get_hour_and_minute() -> str:
    return datetime.now().strftime("%H:%M")

def main() -> typing.NoReturn:
    last_notified_time: str = None

    while True:
        minute = get_minute()
        full_date = get_full_date()
        hour_and_minute = get_hour_and_minute()

        # print(full_date)

        if minute in MINUTES_TO_TRACK and all([hour_and_minute != last_notified_time]):
            print(f"Time: {hour_and_minute} Full Date: {full_date}")
            winsound.PlaySound(NOTIFICATION_SOUND_PATH, winsound.SND_FILENAME)
            last_notified_time = hour_and_minute
        
        time.sleep(TIME_READ_SPEED)

if __name__ == "__main__":
    main()
