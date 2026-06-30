import time

# Get current hour (0-23)
current_hour = int(time.strftime('%H'))

# Get full formatted time to display (HH:MM:SS)
current_time = time.strftime('%H:%M:%S')
print("Current Time:", current_time)

# Greeting Logic
if current_hour < 12:
    print("Good Morning, Subhajit!")
elif current_hour < 16:
    print("Good Afternoon, Subhajit!")
elif current_hour < 20:
    print("Good Evening, Subhajit!")
else:
    print("Good Night, Subhajit!")