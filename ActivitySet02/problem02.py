def add(a, b):
  return(a+b)
  pass
def output(a, b, sum):
  print(f'{a}+{b} is {sum}')
  pass
def main():
  a,b=map(int,input("input? ").split())
  sum= add(a,b)
  output(a, b, sum)
  
main()
#,,,,,
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
