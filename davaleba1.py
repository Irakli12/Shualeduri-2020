def mcd(n1,n2):
  rng = 0
  for i in range(1,n1):  
    f = n1 % i  
    for j in range(1,n2):
      g = n2 % j 
      if (f == 0 and g == 0 and f == g): 
        rng = f  
      else: 
        rng = "not found"
  return rng
