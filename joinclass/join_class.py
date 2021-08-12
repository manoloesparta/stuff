import os
import time
import json
import webbrowser

current_dir = os.path.dirname(__file__)
schedule_file = os.path.join(current_dir, "schedule.json")


def main():
    hour, today = get_time_and_day()
    schedule_today = get_todays_schedule(today)
    if url := get_class_url(schedule_today, hour):
        webbrowser.open(url)


def get_time_and_day():
    now = time.localtime()
    past_class_ended = now.tm_min >= 40 and now.tm_hour % 2 == 1
    hour = str(now.tm_hour + 1) if past_class_ended else str(now.tm_hour)
    today = str(now.tm_wday)
    return hour, today


def get_todays_schedule(today):
    with open(schedule_file, "r") as f:
        schedule = json.load(f)
    return schedule[today]


def get_class_url(schedule_today, hour):
    for subject in schedule_today:
        if hour in subject.split("-"):
            return schedule_today[subject]


if __name__ == "__main__":
    main()
