import numpy as np
import math


class Perceptron:
    def __init__(self, num_inputs,weights=None, bias=-1, learning_rate=0.1, activation_threshold=0.5):
        self.weights = [0.0] * num_inputs
        self.learning_rate = learning_rate

        if weights == None:
            self.weights = np.array([1, 1])
        else:
            self.weights = np.array(weights)
        self.bias = bias
        self.activation_threshold = activation_threshold

    def train(self, training_inputs, labels, epochs=15):
        for i in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                # Ajusta os pesos e o limiar
                self.weights = [w + self.learning_rate * error * i for w, i in zip(self.weights, inputs)]
                self.bias -= self.learning_rate * error

            # print(1)

    def predict(self,  inputs):
        total = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias

        return 1 if total > self.bias else 0


    def custo_mse(self, predict, real_value):
        mse = np.mean((predict - real_value) ** 2)
        return mse


    def _heaviside(self, x):
        """
        Implementa a função delta de heaviside (famoso degrau)
        Essa é uma função de ativação possível para os nós da rede neural.
        """
        return 1 if x >=  self.activation_threshold else 0

    def _sigmoid(self, x):
        """
        Implementa a função sigmoide
        Essa é uma função de ativação possível para os nós da rede neural.
        """
        return 1/(1 + math.exp(-x))

    def _activation(self, perceptron_output):
        """
        Implementação da função de ativação do perceptron
        Escolha uma das funções de ativação possíveis
        """
        return self._heaviside(perceptron_output)

    def forward_pass(self, data):
        """
        Implementa a etapa de inferência (feedforward) do perceptron.
        """
        weighted_sum = self.bias + np.dot(self.weights, data)
        return self._activation(weighted_sum)
    

def main():
    predict_values = []
    
    training_inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
        ]
    
    labels = [0, 1, 1, 0]

    
    
    perceptron = Perceptron(num_inputs= len(training_inputs))
    
    perceptron.train(training_inputs, labels)
    
    for i in range(len(training_inputs)):
        predict_values.append(perceptron.predict(training_inputs[i]))
    
    print(perceptron.custo_mse(np.array(predict_values), np.array(labels)))
    # print(perceptron.predict(training_inputs[2]))
    



if __name__ == "__main__":
    main()