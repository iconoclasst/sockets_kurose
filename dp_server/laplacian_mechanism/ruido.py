from diffprivlib.mechanisms import Laplace

def aplicar_ruido(mensagem):
    idade = float(mensagem['idade'])
    nivel = int(mensagem['nivel'])

    epsilon = 0
    if nivel == 1:
        epsilon=0.4
    elif nivel == 2:
        epsilon=1.0
    elif nivel == 3:
        epsilon=1.5
    
    delta = 0.0
    sensitivity = 0.1

    lap = Laplace(epsilon=epsilon, delta=delta, sensitivity=sensitivity)
    idade_r = lap.randomise(idade)

    return idade_r