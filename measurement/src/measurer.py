import time


class Measurer:
    def __init__(self, name):
        self.name = name
        self.time_measure = {}

    def start_time(self, name):
        self.time_measure[name] = {"start": time.time()}

    def end_time(self, name):
        if name not in self.time_measure:
            raise ValueError(f"{name=} not in {self.time_measure=}")

        self.time_measure[name]["end"] = time.time()

    def time_result(self, name):
        return self.time_measure[name]["end"] - self.time_measure[name]["start"]

    def all_time_result(self, name):
        results = {}
        for time_name in self.time_measure:
            results[time_name] = self.time_result(time_name)

        return results
