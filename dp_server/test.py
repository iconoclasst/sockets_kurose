from diffprivlib.mechanisms import Laplace

a = 5.0

la = Laplace(delta=0.0, sensitivity=0.1, epsilon=1.0)

b = la.randomise(a)
print(b)