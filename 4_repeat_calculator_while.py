while True:
    # 1.Input
    x1 = input("Enter X1: ")
    x2 = input("Enter X2: ")
    op = input("Enter operator: ")
    # 2.Process
    if op == "+":
     sum = int(x1) + int(x2)
    elif op =="-":
     sum = int(x1) - int(x2)
    # 3.Output
    print(f"Sum: {sum}") 