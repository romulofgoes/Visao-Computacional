from equal_de_hist import equalizer
import cv2


"""
    Exemplo com duas imagens na pasta imagem_entrada
    Na pasta imagem_saida, está o resultado de ambas após a equalização
"""

imagem_original = cv2.imread("./imagem_entrada/Questionario-3-Imagem-1.tif") # método da biblioteca Open-Cv que retorna um numpyarray dos pixels e canais da imagem
cv2.imwrite("imagem_saida/Questionario-3-Imagem-1-Equalizada.jpg", equalizer(imagem_original))

imagem_original_2 = cv2.imread("./imagem_entrada/Questionario-3-Imagem-2.tif") # método da biblioteca Open-Cv que retorna um numpyarray dos pixels e canais da imagem
cv2.imwrite("imagem_saida/Questionario-3-Imagem-2-Equalizada.jpg", equalizer(imagem_original_2))