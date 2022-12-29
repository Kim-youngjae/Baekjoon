n = input()
length = len(n)
total = 0

for i in range(length // 2):
    total += int(n[i])
for i in range(length // 2, length):
    total -= int(n[i])
    
if total == 0:
    print("LUCKY")
else:
    print("READY")