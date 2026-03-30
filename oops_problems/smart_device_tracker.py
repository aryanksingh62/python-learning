class SmartDevice:
    def __init__(self,device,status,type_):
        self.device=device
        self.status=status
        self.type=type_

    def show(self):
        return f"{self.device} is {self.status} - {self.type}"
    
    def change_status(self):
        self.status="OFF" if self.status=="ON" else "ON"
        return f"{self.device} is {self.status} - {self.type}"
    
device_1=SmartDevice("AC","ON","whirlpool")
device_2=SmartDevice("FAN","OFF","hitachi")
print(device_1.show())
print(device_1.change_status())
print(device_2.show())
print(device_2.change_status())