from tensorflow.keras.models import load_model # type: ignore
import cv2
import numpy as np

# Carrega o modelo linear
modelo_2 = load_model('modelo_mnist_linear.h5')

def predict_linear():
    # Usa o modelo para realizar uma predição
    img = cv2.imread('./upload/number.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28,28))
    img = img / img.max()
    img = img.reshape(1, 28 * 28)  # Ajusta a imagem para um vetor de 784 elementos
    predicao = modelo_2.predict(img)
    resultado = np.argmax(predicao)
    print(resultado)
    print(predicao)
    return resultado
