for i in range(1, 10):
    # i本身不包含，所以需要+1
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}\t", end='')
    print()