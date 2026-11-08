cnt = 0
age_sum = 0
    
while True:
    age = int(input())
    if age >= 30 or age < 20:
        break
    else:
        cnt += 1
        age_sum += age
        ans = age_sum / cnt

print(f'{ans:.2f}')
