from devices import Device


class Bus:
    def __init__(self, busid = 0):
        self.devices: list[Device] = []
        self.busid = busid

    def add_device(self, device):
        self.devices.append(device)

    def update_devices(self):
        for device in self.devices:
            device.update()

    def __str__(self) -> str:
        return f"Bus {self.busid}:\n{'\n'.join([str(device) for device in self.devices])}"