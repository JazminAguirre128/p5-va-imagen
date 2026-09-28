import cv2
# Leer la imagen con cv2 = computer vision
img = cv2.imread('perro.jpg')
# Determinar el tipo de imagen numpy.ndarray
print(type(img))
#  Mostrar pixeles (148, 240, 3)
print(img.shape)
# Mostrarme imagen en ventana barra de titulo perro0013
cv2.imshow('perro0013', img)
## Tiempo de espera
cv2.waitKey(0)
# Destruir todas las ventanas
cv2.destroyAllWindows()