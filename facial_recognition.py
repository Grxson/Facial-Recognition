import cv2
import numpy

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Para leer una imagen
# img = cv2.imread('img.png')

# Para leer un video
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("video.mp4")

while:
    if img is None:
        print("Se termino el video")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Dibujar rectángulos alrededor de las caras
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Display output
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara
cap.release()

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
