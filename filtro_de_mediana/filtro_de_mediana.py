import numpy as np

def filtro_mediana(imagem: np.ndarray, tam_janela: int):
    

    h, w, c = imagem.shape
    janela_tam = tam_janela # 3X3, 5X5, 7X7, etc
    metade_janela = int(janela_tam/2)
    imagem = imagem[:, :, 0:1] # deixar a imagem com somente um canal
    imagem_nova = imagem.copy() # fazer uma copia da imagem onde o filtro altera os resultados

    for i in range(h-janela_tam):
        for j in range(w-janela_tam):
            arr = np.sort(imagem[i:i+janela_tam, j:j+janela_tam].flatten()) # vetor ordenado dos pixels da janela
            mediana = arr[janela_tam*metade_janela] # mediana
            imagem_nova[i+metade_janela][j+metade_janela][0] = mediana
    return imagem_nova


