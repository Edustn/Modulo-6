from keras.datasets import mnist # type: ignore
from keras.utils import to_categorical # type: ignore
from keras.models import Sequential # type: ignore
from keras.layers import Dense, Flatten, Dropout # type: ignore
from keras.optimizers import Adam # type: ignore
from tensorflow.keras.models import load_model # type: ignore
import cv2
import numpy as np

# Carrega os dados do MNIST
(x_treino, y_treino), (x_teste, y_teste) = mnist.load_data()

# Transforma os labels em one-hot encoding
y_treino_cat = to_categorical(y_treino)
y_teste_cat = to_categorical(y_teste)

# Verificação da saída one-hot encoding
print(y_treino[0]) # Valor da classe
print(y_treino_cat[0]) # Representação one-hot

# Normalização dos dados de entrada
x_treino_norm = x_treino / x_treino.max()
x_teste_norm = x_teste / x_teste.max()

# Reshape dos dados de entrada para formar um vetor de características
x_treino_norm = x_treino_norm.reshape(len(x_treino_norm), 28 * 28)
x_teste_norm = x_teste_norm.reshape(len(x_teste_norm), 28 * 28)

# Criação do modelo totalmente conectado
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compila o modelo
adam = Adam()
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=adam)

# Realiza o treinamento do modelo
historico = model.fit(x_treino_norm, y_treino_cat, epochs=5, validation_split=0.2)

# Salva o modelo
model.save('modelo_mnist_linear.h5')

# Carrega o modelo salvo
modelo_2 = load_model('modelo_mnist_linear.h5')


