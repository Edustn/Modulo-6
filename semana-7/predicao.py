from tensorflow.keras.models import load_model # type: ignore
import cv2
import numpy as np

# Testar o modelo
modelo_2 = load_model('modelo_mnist.h5')

def predict():
    # Usa o modelo para realizar uma predição
    img = cv2.imread('./upload/7.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # predicao = modelo_2.predict(img.reshape(1, 28, 28, 1))
    img = cv2.resize(img, (28,28))
    img = img / img.max()
    # _, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)
    img = img.reshape(1,28,28,1)
    predicao = modelo_2.predict(img)
    # print(predicao)
    print(np.argmax(predicao))
    return np.argmax(predicao)
