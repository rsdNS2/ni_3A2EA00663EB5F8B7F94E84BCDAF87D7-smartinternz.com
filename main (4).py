def fact_rec(n):
  if n==1 or n==0:
    return 1
  else:
    return n*fact_rec(n-1)

number=4
res=fact_rec(number)

print("The factorial of {} is {}".format(number,res))