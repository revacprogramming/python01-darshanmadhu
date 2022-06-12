def f(*args,**kwargs):
  print(args, *args, kwargs)

f(1, 2 , 3, a=2, b=3, c=4)
#python
