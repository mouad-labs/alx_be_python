length = int(input("Enter the size of the pattern:"))
k = 0
while length != k:
  for i in range(1, length + 1):
    for j in range(1, length + 1):
      print("*", end="")

    print()
    k += 1