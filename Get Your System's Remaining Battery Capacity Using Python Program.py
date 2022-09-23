import psutil

battery = psutil.sensors_battery ( )
percent = str(battery.percent)
print("Your device has "+ percent + "% of battery remaining")
