class Memory:
    def __init__(self, size):
        self.size = size
        self.memory = [0x00000000 for _ in range(size)]
    
    def read(self, address):
        if address < 0 or address >= self.size:
            raise ValueError("Address out of range")
        return self.memory[address]

    def write(self, address, data):
        if address < 0 or address >= self.size:
            raise ValueError("Address out of range")
        self.memory[address] = data

    def clear(self):
        self.memory = [0x00000000 for _ in range(self.size)]
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return f"{self.memory}"

    def __del__(self):
        self.memory = None
        del self
