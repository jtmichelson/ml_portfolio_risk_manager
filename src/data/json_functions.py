import json

from src.data.api_calls import JSON_REQUEST
from pathlib import Path


class StockInfo:
    def __init__(self, ticker, entries):
        self.ticker = ticker
        self.entries = entries
        self.filename = "../data/JSON/" + self.ticker + "_stock_data.json"
        self.total_cumulative_gain_string = ""
        self.stock_time_interval = []
        self.gain_list = []
        self.cumulative_gain_list = []
        self.calculate_gains()
        self.calculate_cumulative_gain()

    def find_dates(self):
        try:
            my_abs_path = Path(self.filename).resolve(strict=True)
        except FileNotFoundError:
            print("File does not exist - calling API")
            JSON_REQUEST(self.ticker, "full")
        else:
            with open(self.filename) as json_data:
                handle = json.load(json_data)
                i = 0
                for data in handle["Time Series (Daily)"]:
                    if i < self.entries:
                        self.stock_time_interval.append(data)
                    i += 1
                self.stock_time_interval.reverse()

    def calculate_gains(self):
        i = 0
        previous = 0
        self.find_dates()
        with open(self.filename) as json_data:
            handle = json.load(json_data)
            for day in self.stock_time_interval:
                current = handle["Time Series (Daily)"][day]["4. close"]
                if i == 0:
                    previous = handle["Time Series (Daily)"][day]["4. close"]
                else:
                    gains = ((float(current) - float(previous)) / float(previous))
                    previous = handle["Time Series (Daily)"][day]["4. close"]
                    self.gain_list.append(gains)
                i += 1

    def calculate_cumulative_gain(self):
        i = 0
        cumulative_gain = 0
        for gain in self.gain_list:
            current = gain
            if i == 0:
                previous = gain
                cumulative_gain += gain
            else:
                cumulative_gain += current + (current * previous)
                previous = cumulative_gain
            i += 1
            self.cumulative_gain_list.append(cumulative_gain)
        self.total_cumulative_gain_string = str(round(self.cumulative_gain_list[-1] * 100, 4)) + '%'
