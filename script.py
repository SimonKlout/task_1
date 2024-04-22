import scipy.special

r=int(input("Multiple de Trois ?"))
cube_root = scipy.special.cbrt(r)
print(F'The cube root of {r} is {cube_root} because {cube_root} * {cube_root} * {cube_root} is {r}'
      .format(**{'cube_root': cube_root}))
