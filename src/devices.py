import random


class Device:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.output = None
    
    def get_data(self):
        if id == 0: # Temperature sensor
            self.output = random.randint(18, 23)
        if id == 1: # Movement sensor
            self.output = random.choice([True, False])

    def update(self):
        return self.output

    def __str__(self) -> str:
        return f"Device {self.id}, Address: {self.address}, Output: {self.output}"
