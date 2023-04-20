
import statistics, math

def my_covariance(input_X, input_Y):
    covariance = 0 
    print(f'Input X : {input_X},', f'Input Y : {input_Y}')
    a = len(input_X)

    meanX = statistics.mean(input_X)
    meanY = statistics.mean(input_Y)
    print(f'Mean X : {meanX},', f'Mean Y : {meanY}')

    sum = 0
    for j in range(len(input_X)):
        covariance += (input_X[j]-meanX)*(input_Y[j]-meanY)
    covariance = covariance/a
    return covariance


# 1. Input
input_X = [10,20,30]
input_Y = [12,21,33]

# 2. Process
answer = my_covariance(input_X, input_Y)
answer = round(answer, 2)

# 3. Output
print(f'Answer: {answer}')
