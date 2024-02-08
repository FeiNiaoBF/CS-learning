import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s.strip()
    time_regex = r"(\d{1,2}):?(\d{2})? ([AP]M) to (\d{1,2}):?(\d{2})? ([AP]M)"
    matches = re.search(time_regex, s, re.IGNORECASE)
    if matches:
        time_str = hour12_to_hour24(matches)
        return time_str
    raise ValueError

def hour12_to_hour24(time):
    start_time = time.group(1, 2, 3)
    end_time = time.group(4, 5, 6)
    start_hour, start_minute, start_period = hour12_to_hour24_helper(start_time)
    end_hour, end_minute, end_period = hour12_to_hour24_helper(end_time)
    if start_hour > end_hour and start_period == "AM" and end_period == "PM":
        end_hour += 24
    if start_hour < 0 or start_hour > 23 or end_hour < 0 or end_hour > 23 or start_minute < 0 \
        or start_minute > 59 or end_minute < 0 or end_minute > 59:
        raise ValueError
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

def hour12_to_hour24_helper(time):
    hour, minute = int(time[0]), int(time[1]) if time[1] else None
    period = time[-1]
    if period == "AM" and hour == 12:
        hour = 0
    elif period == "PM" and hour < 12:
        hour += 12
    if minute == None:
        minute = 0
    return hour, minute, period

if __name__ == "__main__":
    main()
