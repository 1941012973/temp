from . import module1 as m1

def differ(a, b):
  largest = m1.largest(a, b)
  
  if largest == a:
    diff = largest - b
  else:
    diff = largest - a
  return diff
