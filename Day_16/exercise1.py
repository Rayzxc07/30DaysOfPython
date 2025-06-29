#Day16ex1
from datetime import datetime, timedelta
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
timestamp = datetime.timestamp(now)
print(f"Current datetime components - Day: {current_day}, Month: {current_month}, Year: {current_year}, Hour: {current_hour}, Minute: {current_minute}")
print(f"Timestamp: {timestamp}")

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted date: {formatted_date}")

time_string = "5 December, 2019"
time_obj = datetime.strptime(time_string, "%d %B, %Y")
print(f"Converted time object: {time_obj}")

new_year = datetime(now.year + 1, 1, 1)
time_diff_new_year = new_year - now
print(f"Time until new year: {time_diff_new_year}")

epoch = datetime(1970, 1, 1)
time_diff_epoch = now - epoch
print(f"Time since epoch: {time_diff_epoch}")
"""
The datetime module is extremely useful for:
- Time series analysis (as mentioned)
- Logging timestamps for application activities
- Scheduling tasks and events
- Age calculation
- Measuring time intervals
- Blog post timestamps
- Financial calculations involving dates
- Calendar applications
- Data analysis with time components
- Handling user input involving dates/times
"""