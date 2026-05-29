import numpy as np

GRAY_SCALE = 256 - 1# (L)

def equalizer(imagem: np.ndarray):
    h, w, c = imagem.shape # pegando o tamanho da largura, altura e canais por pixel da imagem (a ordem é largura e altura?)

    vetor_grayscale = np.zeros(GRAY_SCALE)

    for i in range(h):
        for j in range(w):
            vetor_grayscale[imagem[i][j][0]]+=1 # a imagem está com três canais, mas todos com o mesmo valor

    prob_acumulada = np.zeros(GRAY_SCALE) # lista de propabilidades acumuladas por nível (quanto maior a intensidade de cinza, maior o acúmulo de probabilidades)
    acumulo = 0 # variavel para acumular probabiliadades conforme aumenta a intensidade de cinza
    tam_imagem = h * w 
    for i in range(GRAY_SCALE):
        probabilidade = vetor_grayscale[i]/(tam_imagem)# razão de vezes que aquela intensidade aparece na imagem pelo tamanho da imagem
        acumulo+=probabilidade # o acumulador de probabilidades
        prob_acumulada[i] = acumulo # a lista por intensidade, a começar do zero até o 255, das probabildidades

    for i in range(h):
        for j in range(w):
            """
                altera o pixel da imagem pela equalização de histograma 
                (tamanho de intensidade * o acúmulo de probabilidades até o nível daquela intensidade)
                Ou seja, quanto maior a intensidade, maior o novo valor, quanto menor, menor
            """
            pixel_original = imagem[i][j] #recebe o pixel original
            imagem[i][j] = GRAY_SCALE*prob_acumulada[pixel_original[0]]
    
    return imagem



