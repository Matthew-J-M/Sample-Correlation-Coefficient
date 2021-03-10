#This file is designed to calculate SCC for a given set of INput and Output data
input = (4.53,3.56,4.34,5.06,5.71,4.99,5.29,5.83,4.76,5.61,4.96,4.23)
output = (2.49,2.23,2.51,2.77,3.01,3.05,3.28,3.48,3.13,3.26,2.73,2.62)

input_2 = (2.49,2.23,2.51,2.77,3.01,3.05,3.28,3.48,3.13,3.26,2.73,2.62)
output_2 = (4.53,3.56,4.34,5.06,5.71,4.99,5.29,5.83,4.76,5.61,4.96,4.23)

def mean(dataList):
    tmpValue = 0
    for value in dataList:
        tmpValue = tmpValue + value
    tmpValue = tmpValue / len(dataList)
    return tmpValue

def variance(dataList, mean):
    tmpValue = 0
    for value in dataList:
        tmpValue = tmpValue + (value - mean)*(value - mean)
    tmpValue = tmpValue / len(dataList)
    return tmpValue

mean_input_1 = mean(input)
mean_output_1 = mean(output)
variance_input_1 = variance(input, mean_input_1)
variance_output_1 = variance(output, mean_output_1)

mean_input_2 = mean(input_2)
mean_output_2 = mean(output_2)
variance_input_2 = variance(input_2, mean_input_2)
variance_output_2 = variance(output_2, mean_output_2)

def SCC(inputList, outputList, meanInput, meanOutput, varianceInput, varianceOutput):
    tmpValue = 0
    for num in range(len(input)):
        x = inputList.__getitem__(num)
        y = outputList.__getitem__(num)
        value = (x-meanInput)*(y-meanOutput)/(varianceInput*varianceOutput)
        tmpValue = tmpValue + value
    tmpValue = tmpValue / (len(inputList) - 1)
    return tmpValue

result_1 = SCC(input, output, mean_input_1, mean_output_1, variance_input_1, variance_output_1)
result_2 = SCC(input_2, output_2, mean_input_2, mean_output_2, variance_input_2, variance_output_2)
print(result_1)
print(result_2)