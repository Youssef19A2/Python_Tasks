'''
% Battery and make Notification
'''
import psutil
from plyer import notification
import time

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    status = "Charging" if plugged else "Not Charging"

    notification.notify(
        title="Battery Status",
        message=f"Battery Percentage: {percent}%\nStatus: {status}",
        timeout=5  
    )
    
    time.sleep(60)  
