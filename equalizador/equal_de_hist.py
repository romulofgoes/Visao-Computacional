import numpy as np

GRAY_SCALE = 256 - 1# (L)

def equalizer(imagem: np.ndarray):

    """
        Objetiva alterar o pixel da imagem pela equalização de histograma.

        Faz-se o PRODUTO do tamanho de intensidade vezes o acúmulo de probabilidades até o nível daquela intensidade.
        Ou seja, quanto maior a intensidade, maior o novo valor, quanto menor, menor.

        Args:
            imagem(numpy.ndarray): matriz da imagem (altura, largura, canais) em que se faz o vetor probabilidade

        Returns:
            numpy.ndarray: nova matriz de imagem (altura, largura, 1) com somente um canal já equalizado, com maior contraste.


    """


    h, w, c = imagem.shape # pegando o tamanho da largura, altura e canais por pixel da imagem (a ordem é largura e altura?)
    vetor_grayscale = np.zeros(GRAY_SCALE)

    prob_acumulada = np.zeros(GRAY_SCALE) # lista de propabilidades acumuladas por nível (quanto maior a intensidade de cinza, maior o acúmulo de probabilidades)
    acumulo = 0 # variavel para acumular probabiliadades conforme aumenta a intensidade de cinza
    tam_imagem = h * w 

    for i in range(h):
        for j in range(w):
            vetor_grayscale[imagem[i][j][0]]+=1 # a imagem está com três canais, mas todos com o mesmo valor

    for i in range(GRAY_SCALE):
        probabilidade = vetor_grayscale[i]/(tam_imagem)# razão de vezes que aquela intensidade aparece na imagem pelo tamanho da imagem
        acumulo+=probabilidade # o acumulador de probabilidades
        prob_acumulada[i] = acumulo # a lista por intensidade, a começar do zero até o 255, das probabildidades
    
    for i in range(h):
        for j in range(w):
            pixel_original = imagem[i][j] #recebe o pixel original
            imagem[i][j] = GRAY_SCALE*prob_acumulada[pixel_original[0]]
    
    return imagem



