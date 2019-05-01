import json
import urllib.request

def JSON_REQUEST(ticker, output_size):
    with open("../config/API_KEY.json") as api_key_file:
        handle = json.load(api_key_file)
        apikey = handle["API_KEY"]
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=" + output_size + "&apikey=" + apikey
    data = urllib.request.urlopen(url)
    output = json.load(data)
    filename = "../data/JSON/" + ticker + "_stock_data.json"
    with open(filename, 'w') as outfile:
        json.dump(output, outfile, indent=4)
