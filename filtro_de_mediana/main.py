import cv2
from filtro_de_mediana import filtro_mediana

imagem_original = cv2.imread("Questionario-3-Imagem-3.tif")
for i in range(3,7+1,2):
    cv2.imwrite(f"imagem/Questionario-3-imagem-janela-{i}.jpg", filtro_mediana(imagem_original, i))