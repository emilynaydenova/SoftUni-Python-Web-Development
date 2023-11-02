from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        # self.time_obj = datetime(100, 1, 1, hour=hours, minute=minutes, second=seconds)

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        # self.time_obj += timedelta(seconds=1)
        # self.hours = self.time_obj.hour
        # self.minutes = self.time_obj.minute
        # self.seconds = self.time_obj.second
        self.seconds += 1
        self.update_time()
        return self.get_time()

    def update_time(self):
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return

timem = Time(9, 30, 59)
print(timem.next_second())
timem = Time(10, 59, 59)
print(timem.next_second())
timem = Time(23, 59, 59)
print(timem.next_second())

# -----------------

import datetime

x = datetime.datetime.now()
print(x)  # 2020-07-07 19:50:12.529700
print(f'{x.day:02d}.{x.month:02d}.{x.year:04d}')  # 07.07.2020
print(x.strftime("%B"))  # July

# Directive	Description	Example	Try it
# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%

t = datetime.time(hour=23, minute=59, second=59)
print(t)  # 23:59:59
