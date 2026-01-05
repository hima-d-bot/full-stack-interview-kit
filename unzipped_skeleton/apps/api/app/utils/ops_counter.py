class OpsCounter:
    def __init__(self):
        self.count = 0

    def increment(self, amount: int = 1):
        self.count += amount

    def reset(self):
        self.count = 0

    def get_count(self) -> int:
        return self.count

ops_counter = OpsCounter()
