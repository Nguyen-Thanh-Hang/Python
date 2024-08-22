import random
def ucln_euclid(num1 ,num2):
    if (num2 == 0):
      return num1
#Nếu num2 khác 0 thì tìm UCLN của num2 và số dư của num1 cho num2
    else:
        return ucln_euclid(num2, num1 % num2)
    # Lấy ngẫu nhiên hai số
N = 10**6
num1 = random.randint(1, N)
num2 = random.randint(1, N)
# Tính và in kết quả
result = ucln_euclid(num1, num2)
print(f"ƯCLN của {num1} và {num2} là: {result}")

import math
import random

def experiment(N, num_trials):
    count = 0
    for i in range(0, N+1):
        num1 = random.randint(1, N)
        num2 = random.randint(1, N)
        if math.gcd(num1, num2) == 1:
            count += 1
    return count / num_trials

num_trials = 10**6
N = 10**6
P = experiment(N, num_trials)
print("Xác suất P =", P)

#Output: ƯCLN của 411039 và 577727 là 1
#        Xác suất P = 0.607851
