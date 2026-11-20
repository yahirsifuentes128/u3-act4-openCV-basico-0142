
# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2
import numpy as np
import sys

print("---+ Yahir Sifuentes NC:0142 +---")

# ==============================================================================
# 1. LECTURA DE LA IMAGEN
# ==============================================================================
print("\n---+ 1. LECTURA DE IMÁGENES (Yahir 0142) +---")
nombre_ventana = 'GPO3H: Talonflame de Ash 0142'
imgTalonflame = cv2.imread('Talonflame_de_Ash_0142.png')

if imgTalonflame is None:
    print("Error: No se pudo leer Talonflame_de_Ash_0142.png")
    sys.exit()
else:
    print("Imagen cargada exitosamente.")

cv2.namedWindow(nombre_ventana)

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n---+ 2. PROPIEDADES DE LA IMAGEN (Yahir 0142) +---")
height, width, channels = imgTalonflame.shape
print(f"Dimensiones: {width}x{height} píxeles")
print(f"Número de canales: {channels}")
print(f"Tipo de dato: {imgTalonflame.dtype}")
print(f"Total de datos/píxeles: {imgTalonflame.size}")

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n---+ 3. IMAGEN ORIGINAL DE TALONFLAME (Yahir 0142) +---")
print("Presiona cualquier tecla para continuar...")
cv2.imshow(nombre_ventana, imgTalonflame)
cv2.waitKey(0)

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES
# ==============================================================================
print("\n---+ 4. MODIFICANDO PÍXELES (Yahir 0142) +---")
pixel_img = imgTalonflame.copy()
x, y = width // 2, height // 2
pixel = pixel_img[y, x]
print(f"Valor del píxel en ({x}, {y}): {pixel} (BGR)")
pixel_img[y, x] = [0, 0, 255]
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)
cv2.imshow('Pixel Modificado (Yahir 0142)', pixel_img)
cv2.waitKey(0)

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI)
# ==============================================================================
print("\n---+ 5. REGIÓN DE INTERÉS ROI (Yahir 0142) +---")
roi_img = imgTalonflame.copy()
x1, y1 = width // 4, height // 4
x2, y2 = (width * 3) // 4, (height * 3) // 4
roi = roi_img[y1:y2, x1:x2]
cv2.rectangle(roi_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('Imagen con ROI marcada (Yahir 0142)', roi_img)
cv2.waitKey(0)
cv2.imshow('ROI Extraida (Yahir 0142)', roi)
cv2.waitKey(0)

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES BGR
# ==============================================================================
print("\n---+ 6. SEPARANDO Y FUSIONANDO CANALES (Yahir 0142) +---")
b, g, r = cv2.split(imgTalonflame)
cv2.imshow('Canal Azul (Yahir 0142)', b)
cv2.imshow('Canal Verde (Yahir 0142)', g)
cv2.imshow('Canal Rojo (Yahir 0142)', r)
cv2.waitKey(0)

zeros = np.zeros_like(b)
blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])
cv2.imshow('Azul Coloreado (Yahir 0142)', blue_img)
cv2.imshow('Verde Coloreado (Yahir 0142)', green_img)
cv2.imshow('Rojo Coloreado (Yahir 0142)', red_img)
cv2.waitKey(0)

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES
# ==============================================================================
print("\n---+ 7. REDIMENSIONANDO IMÁGENES (Yahir 0142) +---")
resized_img = cv2.resize(imgTalonflame, (400, 300))
cv2.imshow('Redimensionada 400x300 (Yahir 0142)', resized_img)
cv2.waitKey(0)

half_size = cv2.resize(imgTalonflame, None, fx=0.5, fy=0.5)
double_size = cv2.resize(imgTalonflame, None, fx=1.5, fy=1.5)
cv2.imshow('Mitad de tamano 0.5x (Yahir 0142)', half_size)
cv2.waitKey(0)
cv2.imshow('Ampliada 1.5x (Yahir 0142)', double_size)
cv2.waitKey(0)

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n---+ 8. ROTANDO IMÁGENES (Yahir 0142) +---")
height, width = imgTalonflame.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
rotated_img = cv2.warpAffine(imgTalonflame, rotation_matrix, (width, height))
cv2.imshow('Imagen Rotada 45 grados (Yahir 0142)', rotated_img)
cv2.waitKey(0)

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES
# ==============================================================================
print("\n---+ 9. VOLTEANDO IMÁGENES (Yahir 0142) +---")
horizontal_flip = cv2.flip(imgTalonflame, 1)
cv2.imshow('Volteo Horizontal (Yahir 0142)', horizontal_flip)
cv2.waitKey(0)

vertical_flip = cv2.flip(imgTalonflame, 0)
cv2.imshow('Volteo Vertical (Yahir 0142)', vertical_flip)
cv2.waitKey(0)

both_flip = cv2.flip(imgTalonflame, -1)
cv2.imshow('Volteo en Ambos Ejes (Yahir 0142)', both_flip)
cv2.waitKey(0)

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n---+ 10. GUARDANDO RESULTADOS (Yahir 0142) +---")
result = cv2.imwrite('Talonflame_rotada_0142.png', rotated_img)

if result:
    print("Imagen rotada guardada exitosamente.")
else:
    print("Error: No se pudo guardar la imagen.")

cv2.destroyAllWindows()
print("\n---+ ¡Operaciones completadas! Yahir Sifuentes NC:0142 +---")
