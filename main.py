#Author : Sudip Mitra
for i in range(int(input())):
  n = int(input())
  if n<4 :
    print(0)
  else :
    if n % 2 == 0 :
      n = n - 2
    else :
      n = n - 3
    k = n // 2
    print (k * ( k + 1) // 2)
