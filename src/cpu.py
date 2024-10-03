from boards import BOARDS
from gpio import Gpio
from memory import Memory
from bus import Bus
from devices import Device


class Cpu:
    def __init__(self, id):
        if id in BOARDS:
            self.board = BOARDS[id]
        else:
            raise ValueError(f"Invalid board ID: {id}")
        
        self.gpio = []
        
        for i in range(len(self.board['gpio'])):
            self.gpio.append(Gpio(i, self.board['gpio'][i]))
            
        self.memory = Memory(self.board['ram'])
        self.step = 0
        self.registers = {'A': 0, 'B': 0, 'X': 0, 'Y': 0, 'PC': 0, 'SP': 0, 'PSW': 0, 'IR': 0, 'FLAGS': 0}
        self.bus = Bus()
    
    def update(self):
        self.step += 1
        #opcode = self.memory.read(self.registers['PC'])
        self.registers['PC'] += 1
        
        self.bus.update_devices()
    
    def __str__(self):
        return f"{self.gpio}"

    def __repr__(self):
        return f"{self.step}\n" \
               f"Memory: {self.memory}\n" \
               f"Registers: {self.registers}\n" \
               f"GPIO: \n{'\n'.join([repr(pin) for pin in self.gpio])}\n" \
               f"{self.bus}"

    def get_info(self):
        return f"Board: {cpu.board['name']}\n" \
               f"RAM: {cpu.board['ram']} KB\n" \
               f"Flash: {cpu.board['flash']} KB\n" \
               f"EEPROM: {cpu.board['eeprom']} KB\n" \
               f"GPIO:\n{'\n'.join([repr(pin) for pin in self.gpio])}"


if __name__ == "__main__":
    cpu = Cpu(0)
    
    print(cpu.get_info())
    print(repr(cpu))
    cpu.memory.clear()
    
    tmp = Device(0, 0x00)
    
    cpu.bus.add_device(tmp)
    
    print(repr(cpu))
    
    for _ in range(100):
        cpu.update()
        print(repr(cpu))