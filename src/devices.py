import random


class Device:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.output = None
    
    def get_date(self):
        if id == 0: # Temperature sensor
            return random.randint(18, 23)
        if id == 1: # Movement sensor
            return random.choice([True, False])

    def update(self):
        self.output = self.get_data()

    def __str__(self) -> str:
        return f"Device {self.id}, Address: {self.address}, Output: {self.output}"
