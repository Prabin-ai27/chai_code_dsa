device_status="Active"
device_temp=38

if device_status=="Active":
    if device_temp>35:
        print("Device is Hight Tempreture")
        pass
    else:
        print("Tempreature in Normal")
    
else:
    print("Device is Offline")