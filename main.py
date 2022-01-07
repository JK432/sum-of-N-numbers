#  Write a program that reads an integer N from the keyboard and then calls a user defined function to compute and displays the sum of the numbers from N to (2*N ) if N is non negative. if n is negative then displays the sum of the numbers from (2* N) to N. The satrting and ending points are included in the sum 
def sumn(n):
  sum=0
  for i in range (n,2*n+1):
    sum=sum+i
  print(sum)
x=int(input())
sumn(x)

