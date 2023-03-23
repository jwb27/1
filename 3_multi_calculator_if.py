
import math
# 1.Input

x1 = input("Enter X1: ")
x2 = input("Enter X2: ")
x3 = input("Enter X3: ")
op = input("Enter operator: ")

# 2.Process
if op == "+":
    sum = int(x1) + int(x2)
elif op =="-":
    sum = int(x1) - int(x2)
elif op =="*":
    sum = int(x1) * int(x2)
elif op =="/":
    sum = int(x1) / int(x2)
elif op =="avg":
    sum = (int(x1) + int(x2))/2
elif op =="SD":
    mean = (int(x1) + int(x2) + int(x3))/3
    step1 = int(x1) - mean
    step2 = int(x2) - mean
    step3 = int(x3) - mean
    step4 = (step1)**2 + (step2)**2 + (step3)**2
    sum = math.sqrt(step4/3)



# 3.Output

print(f"Sum: {sum}")
