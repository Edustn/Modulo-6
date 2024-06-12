from keras.datasets import mnist # type: ignore
from keras.utils import to_categorical # type: ignore
from keras.models import Sequential # type: ignore
#Camadas que serão utilizadas
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout # type: ignore
from keras.optimizers import Adam # type: ignore
# Carrega o modelo
from tensorflow.keras.models import load_model # type: ignore
import cv2
import numpy as np



# print('Entrando no treino')
# (x_treino, y_treino), (x_teste, y_teste) = mnist.load_data()
# print('Finalizei o treino')



# # Trazendo a função `to_categorical` para transformar os labels em one-hot encoding
# y_treino_cat = to_categorical(y_treino)
# y_teste_cat = to_categorical(y_teste)

# # Verificação da saída one-hot encoding
# print(y_treino[0]) #Valor da classe
# print(y_treino_cat[0]) #Representação onehot

# # Normalização dos dados de entrada
# x_treino_norm = x_treino/x_treino.max()
# x_teste_norm = x_teste/x_teste.max()

# # Reshape dos dados de entrada para adicionar o canal de cor
# x_treino = x_treino.reshape(len(x_treino), 28, 28, 1)
# x_treino_norm = x_treino_norm.reshape(len(x_treino_norm), 28, 28, 1)
# x_teste = x_teste.reshape(len(x_teste), 28, 28, 1)
# x_teste_norm = x_teste_norm.reshape(len(x_teste_norm), 28, 28, 1)


# #Modelo da rede


# # Criação do modelo LeNet5
# model = Sequential()
# model.add(Conv2D(filters=32, kernel_size=(5,5), padding='same', activation='relu', input_shape=(28, 28, 1)))
# model.add(MaxPool2D(strides=2))
# model.add(Conv2D(filters=48, kernel_size=(5,5), padding='valid', activation='relu'))
# model.add(MaxPool2D(strides=2))
# model.add(Flatten())
# model.add(Dense(256, activation='relu'))
# model.add(Dense(84, activation='relu'))
# model.add(Dense(10, activation='softmax'))

# # Constroi o modelo
# model.build()

# # print("Já construi o modelo")

# #Compila o modelo
# adam = Adam()
# model.compile(loss='categorical_crossentropy',
#               metrics=['accuracy'], optimizer=adam)

# # Realiza o treinamento do modelo
# historico = model.fit(x_treino_norm, y_treino_cat, epochs=5, validation_split=0.2)

# model.save('modelo_mnist.h5')

# Testar o modelo
modelo_2 = load_model('modelo_mnist.h5')


# Usa o modelo para realizar uma predição
img = cv2.imread('./upload/7.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# predicao = modelo_2.predict(img.reshape(1, 28, 28, 1))
img = cv2.resize(img, (28,28))
img = img / img.max()
# _, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)
img = img.reshape(1,28,28,1)
predicao = modelo_2.predict(img)
print(predicao)
print(np.argmax(predicao))
