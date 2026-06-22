from diffprivlib.mechanisms import Gaussian

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

    gau = Gaussian(epsilon=epsilon, delta=delta, sensitivity=sensitivity)
    idade_r = gau.randomise(idade)

    return idade_r