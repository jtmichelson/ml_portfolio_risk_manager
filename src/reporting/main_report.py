from src.model.epsilon_greedy import StockHistoryArm, EpsilonGreedy
from src.model.follow_the_regularized_leader import FollowTheRegularizedLeader
from src.data.json_functions import StockInfo
from src.reporting.report_helpers import epsilon_greedy_output_formatted, ftrl_output_formatted

number_of_entries = 1000

apple = StockInfo("AAPL", number_of_entries)
print(apple.ticker + ": " + apple.total_cumulative_gain_string)

microsoft = StockInfo("MSFT", number_of_entries)
print(microsoft.ticker + ": " + microsoft.total_cumulative_gain_string)

intel = StockInfo("INTC", number_of_entries)
print(intel.ticker + ": " + intel.total_cumulative_gain_string)

google = StockInfo("GOOGL", number_of_entries)
print(google.ticker + ": " + google.total_cumulative_gain_string)

amazon = StockInfo("AMZN", number_of_entries)
print(amazon.ticker + ": " + amazon.total_cumulative_gain_string)

stock_set_increasing = [apple.gain_list, google.gain_list, amazon.gain_list, intel.gain_list, microsoft.gain_list]
arms = list(map(lambda mu: StockHistoryArm(mu), stock_set_increasing))

f = open("../data/output/epsilon_greedy_increasing_stocks.csv", "w")

for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
    epsilon_greedy_instance = EpsilonGreedy(epsilon, [], [])
    results = epsilon_greedy_output_formatted(epsilon_greedy_instance, arms, number_of_entries - 1)
    for i in range(len(results[0])):
        f.write(str(epsilon) + ',' + str(results[0][i]) + ',' + str(results[1][i]) + ',' + str(round(results[2][i], 4)) + ',' + str(round(results[3][i], 4)) + '\n')

f.close()

f = open("../data/output/ftrl_increasing_stocks_opg.csv", "w")

ftr1_instance1 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance2 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance3 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance4 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance5 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])

ftrl_instances = [ftr1_instance1, ftr1_instance2, ftr1_instance3, ftr1_instance4, ftr1_instance5]

results = ftrl_output_formatted(ftrl_instances, stock_set_increasing, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftr1_instance1
del ftr1_instance2
del ftr1_instance3
del ftr1_instance4
del ftr1_instance5
del ftrl_instances
del results

f.close()

f = open("../data/output/ftl_increasing_stocks.csv", "w")

ftr1_instance1 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftr1_instance2 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftr1_instance3 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftr1_instance4 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftr1_instance5 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])

ftrl_instances = [ftr1_instance1, ftr1_instance2, ftr1_instance3, ftr1_instance4, ftr1_instance5]

results = ftrl_output_formatted(ftrl_instances, stock_set_increasing, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftr1_instance1
del ftr1_instance2
del ftr1_instance3
del ftr1_instance4
del ftr1_instance5
del ftrl_instances
del results

f.close()

f = open("../data/output/ftrl_increasing_stocks_rda.csv", "w")

ftr1_instance1 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance2 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance3 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance4 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftr1_instance5 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])

ftrl_instances = [ftr1_instance1, ftr1_instance2, ftr1_instance3, ftr1_instance4, ftr1_instance5]

results = ftrl_output_formatted(ftrl_instances, stock_set_increasing, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftr1_instance1
del ftr1_instance2
del ftr1_instance3
del ftr1_instance4
del ftr1_instance5
del ftrl_instances

f.close()


number_of_entries = 950

twitter = StockInfo("TWTR", number_of_entries)
print(twitter.ticker + ": " + twitter.total_cumulative_gain_string)

tesla = StockInfo("TSLA", number_of_entries)
print(tesla.ticker + ": " + tesla.total_cumulative_gain_string)

fitbit = StockInfo("FIT", number_of_entries)
print(fitbit.ticker + ": " + fitbit.total_cumulative_gain_string)

altaba = StockInfo("AABA", number_of_entries)
print(altaba.ticker + ": " + altaba.total_cumulative_gain_string)

general_electric = StockInfo("GE", number_of_entries)
print(general_electric.ticker + ": " + general_electric.total_cumulative_gain_string)

stock_set_mixed = [twitter.gain_list, altaba.gain_list, general_electric.gain_list, fitbit.gain_list, tesla.gain_list]
arms = list(map(lambda mu: StockHistoryArm(mu), stock_set_mixed))


f = open("../data/output/epsilon_greedy_mixed_stocks.csv", "w")

for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
    epsilon_greedy_instance = EpsilonGreedy(epsilon, [], [])
    results = epsilon_greedy_output_formatted(epsilon_greedy_instance, arms, number_of_entries - 1)
    for i in range(len(results[0])):
        f.write(str(epsilon) + ',' + str(results[0][i]) + ',' + str(results[1][i]) + ',' + str(round(results[2][i], 4)) + ',' + str(round(results[3][i], 4)) + '\n')

f.close()

f = open("../data/output/ftrl_mixed_stocks_opg.csv", "w")

ftrl_instance6 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance7 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance8 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance9 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance10 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])

ftrl_instances2 = [ftrl_instance6, ftrl_instance7, ftrl_instance8, ftrl_instance9, ftrl_instance10]

results = ftrl_output_formatted(ftrl_instances2, stock_set_mixed, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftrl_instance6
del ftrl_instance7
del ftrl_instance8
del ftrl_instance9
del ftrl_instance10
del ftrl_instances2
del results

f.close()


f = open("../data/output/ftl_mixed_stocks.csv", "w")

ftrl_instance6 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance7 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance8 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance9 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance10 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])

ftrl_instances2 = [ftrl_instance6, ftrl_instance7, ftrl_instance8, ftrl_instance9, ftrl_instance10]

results = ftrl_output_formatted(ftrl_instances2, stock_set_mixed, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftrl_instance6
del ftrl_instance7
del ftrl_instance8
del ftrl_instance9
del ftrl_instance10
del ftrl_instances2
del results

f.close()

f = open("../data/output/ftrl_mixed_stocks_rda.csv", "w")

ftrl_instance6 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance7 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance8 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance9 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance10 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])

ftrl_instances2 = [ftrl_instance6, ftrl_instance7, ftrl_instance8, ftrl_instance9, ftrl_instance10]

results = ftrl_output_formatted(ftrl_instances2, stock_set_mixed, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftrl_instance6
del ftrl_instance7
del ftrl_instance8
del ftrl_instance9
del ftrl_instance10
del ftrl_instances2
del results

f.close()

number_of_entries = 950

qualcomm = StockInfo("QCOM", number_of_entries)
print(qualcomm.ticker + ": " + qualcomm.total_cumulative_gain_string)

sony = StockInfo("SNE", number_of_entries)
print(sony.ticker + ": " + sony.total_cumulative_gain_string)

cisco = StockInfo("CSCO", number_of_entries)
print(cisco.ticker + ": " + cisco.total_cumulative_gain_string)

activision = StockInfo("ATVI", number_of_entries)
print(activision.ticker + ": " + activision.total_cumulative_gain_string)

xilinx = StockInfo("XLNX", number_of_entries)
print(xilinx.ticker + ": " + xilinx.total_cumulative_gain_string)

stock_set_big = [apple.gain_list, google.gain_list, amazon.gain_list, intel.gain_list, microsoft.gain_list, twitter.gain_list, altaba.gain_list, general_electric.gain_list, fitbit.gain_list, tesla.gain_list, qualcomm.gain_list, sony.gain_list, cisco.gain_list, activision.gain_list, xilinx.gain_list]
arms = list(map(lambda mu: StockHistoryArm(mu), stock_set_big))

f = open("../data/output/epsilon_greedy_big_stocks.csv", "w")

for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
    epsilon_greedy_instance = EpsilonGreedy(epsilon, [], [])
    results = epsilon_greedy_output_formatted(epsilon_greedy_instance, arms, number_of_entries - 1)
    for i in range(len(results[0])):
        f.write(str(epsilon) + ',' + str(results[0][i]) + ',' + str(results[1][i]) + ',' + str(round(results[2][i], 4)) + ',' + str(round(results[3][i], 4)) + '\n')

f.close()

f = open("../data/output/ftl_big_stocks.csv", "w")

ftrl_instance1 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance2 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance3 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance4 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance5 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance6 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance7 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance8 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance9 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance10 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance11 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance12 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance13 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance14 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])
ftrl_instance15 = FollowTheRegularizedLeader(0.05, 1.0, 0.0, 0.0, 1, "OPG", [0])

ftrl_instances3 = [ftrl_instance1, ftrl_instance2, ftrl_instance3, ftrl_instance4, ftrl_instance5, ftrl_instance6, ftrl_instance7, ftrl_instance8, ftrl_instance9, ftrl_instance10, ftrl_instance11, ftrl_instance12, ftrl_instance13, ftrl_instance14, ftrl_instance15]

results = ftrl_output_formatted(ftrl_instances3, stock_set_big, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftrl_instance1
del ftrl_instance2
del ftrl_instance3
del ftrl_instance4
del ftrl_instance5
del ftrl_instance6
del ftrl_instance7
del ftrl_instance8
del ftrl_instance9
del ftrl_instance10
del ftrl_instance11
del ftrl_instance12
del ftrl_instance13
del ftrl_instance14
del ftrl_instance15
del ftrl_instances3
del results

f.close()


f = open("../data/output/ftrl_big_stocks_rda.csv", "w")

ftrl_instance1 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance2 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance3 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance4 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance5 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance6 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance7 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance8 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance9 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance10 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance11 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance12 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance13 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance14 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])
ftrl_instance15 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "RDA", [0])

ftrl_instances3 = [ftrl_instance1, ftrl_instance2, ftrl_instance3, ftrl_instance4, ftrl_instance5, ftrl_instance6, ftrl_instance7, ftrl_instance8, ftrl_instance9, ftrl_instance10, ftrl_instance11, ftrl_instance12, ftrl_instance13, ftrl_instance14, ftrl_instance15]

results = ftrl_output_formatted(ftrl_instances3, stock_set_big, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftrl_instance1
del ftrl_instance2
del ftrl_instance3
del ftrl_instance4
del ftrl_instance5
del ftrl_instance6
del ftrl_instance7
del ftrl_instance8
del ftrl_instance9
del ftrl_instance10
del ftrl_instance11
del ftrl_instance12
del ftrl_instance13
del ftrl_instance14
del ftrl_instance15
del ftrl_instances3
del results

f.close()

f = open("../data/output/ftrl_big_stocks_opg.csv", "w")

ftrl_instance1 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance2 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance3 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance4 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance5 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance6 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance7 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance8 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance9 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance10 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance11 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance12 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance13 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance14 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])
ftrl_instance15 = FollowTheRegularizedLeader(0.05, 1.0, 1.0, 1.0, 1, "OPG", [0])

ftrl_instances3 = [ftrl_instance1, ftrl_instance2, ftrl_instance3, ftrl_instance4, ftrl_instance5, ftrl_instance6, ftrl_instance7, ftrl_instance8, ftrl_instance9, ftrl_instance10, ftrl_instance11, ftrl_instance12, ftrl_instance13, ftrl_instance14, ftrl_instance15]

results = ftrl_output_formatted(ftrl_instances3, stock_set_big, number_of_entries - 1)

for i in range(len(results[0])):
    f.write(str(results[0][i]) + "," + str(results[1][i]) + "," + str(round(results[2][i], 4)) + "," + str(round(results[3][i], 4)) + "\n")

del ftrl_instance1
del ftrl_instance2
del ftrl_instance3
del ftrl_instance4
del ftrl_instance5
del ftrl_instance6
del ftrl_instance7
del ftrl_instance8
del ftrl_instance9
del ftrl_instance10
del ftrl_instance11
del ftrl_instance12
del ftrl_instance13
del ftrl_instance14
del ftrl_instance15
del ftrl_instances3
del results

f.close()
