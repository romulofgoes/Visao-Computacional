from equalizador.equal_de_hist import equalizer
import cv2
def main():
    
    imagem_original = cv2.imread("./Questionario-3-Imagem-1.tif") # método da biblioteca Open-Cv que retorna um numpyarray dos pixels e canais da imagem
    cv2.imwrite("Questionario-3-Imagem-1-Equalizada.jpg", equalizer(imagem_original))

    imagem_original_2 = cv2.imread("./Questionario-3-Imagem-2.tif") # método da biblioteca Open-Cv que retorna um numpyarray dos pixels e canais da imagem
    cv2.imwrite("Questionario-3-Imagem-2-Equalizada.jpg", equalizer(imagem_original_2))