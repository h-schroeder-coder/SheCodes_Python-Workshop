
## lesson 2

# Import datetime
from datetime import datetime

# Display the current date and time (no formatting)
now = datetime.now()
print(now)

# Display the current date and time following this format: Date: Jan 12, 2032 Time: 14:03
formatted_date = now.strftime("Date: %b %d, %Y Time: %H:%M")
print(formatted_date)

# Convert this time stamp 1705590204 into a date and display only the time using this format: 2:30am
from datetime import datetime
timestamp = 1705590204
date = datetime
date_from_timestamp = date.fromtimestamp(timestamp)
print(date_from_timestamp)
