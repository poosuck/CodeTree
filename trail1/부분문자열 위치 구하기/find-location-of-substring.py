input_str = input()
target_str = input()

# Please write your code here.

ans = -1

for i in range(len(input_str)):
    if input_str[i:i+len(target_str)] == target_str:
        ans = i
        break

print(ans)