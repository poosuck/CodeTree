A, B = map(int, input().split())

ans = (A * 10**20) // B

print(f'{ans // 10**20}.{ans % 10**20:020d}')