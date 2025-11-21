print("Nhap cac dong van ban(nhap done de -> ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    line.append(line)
print("Cac dong da nhap sau khi chuyen chu in hoa:")
for line in lines:
    print(line.upper())    