class Gpio:
    def __init__(self, pin, state = 0) -> None:
        self.pin = pin
        self.state = state

    def __repr__(self) -> str:
        return f"{self.pin}: {self.state}"
