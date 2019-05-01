# Financial Portfolio Risk Manager

## Abstract
* We look at the application of Online Convex Optimization (OCO) techniques to portfolio risk management. Three main approaches will be compared: Follow-The-Leader (FTL), Follow-The-Regularized-Leader (FTRL), and Epsilon-Greedy. The focus will be on the behavior of the FTRL implementation using Online Proximal Gradient Descent (OPGD) and Regularized Dual Averaging (RDA) regularization functions. Our sample sets consist of multiple small subsets of securities of varying nature. We run our algorithm incrementally over historical data deciding the optimal investment candidate at each end-of-day. The algorithm has no knowledge of the future day’s result during its prediction phase and therefore can be directly applied to real-time data. The cumulative percentage gain over time of each run is baselined against the average of each set. Each model is then evaluated to decide if it produces a statistically significant greater reward than random choice.

## Getting Started
* Get your own personal API Key from www.alphavantage.co
* Go to src/config/API_KEY.json and put in your API Key.
* Run main_report.py to generate csv reports
* Add new stocks to main_report.py and it will call the API and save the historical data locally in src/data/JSON

## Testing
* TBD

## License
* See ~/LICENSE