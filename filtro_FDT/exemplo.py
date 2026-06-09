import cv2
import numpy as np
from mask import mask

img_src = cv2.imread("imagens/Questionario-3-Imagem-4.png") #importa a imagem
img_src = img_src[:, :, 0] # como já está em grayscale, só tranforma em 1 só canal

f = np.fft.fft2(img_src) # faz a FFT de duas dimensões da imagem original
fshift = np.fft.fftshift(f) # coloca o componente da frequência zero no centro do espectro
img_src = np.log(np.abs(fshift))*20 # pega a magnitude da expressão complexa, achata os valores com np.log e amplifica com o produto de 20

fshift = mask(img_src, fshift, 40, 220, 255)

f_ishift = np.fft.ifftshift(fshift) #faz a inversa do fshift
img_out = np.fft.ifft2(f_ishift) # voltra a imagem do domínio da frequência para o domínio espacial
img_out = np.abs(img_out) # pega as magnitudes do valor gerado

cv2.imwrite("imagens/output.jpg", img_out)




