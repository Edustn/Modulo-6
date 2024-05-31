class Perceptron:
    def __init__(self, num_inputs, threshold=0, learning_rate=0.1):
        self.weights = [0.0] * num_inputs
        self.threshold = threshold
        self.learning_rate = learning_rate

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        total = sum(w * i for w, i in zip(self.weights, inputs))
        # zip_2 = zip(self.weights, inputs)
        # print(zip_2)
        # Aplica a função degrau para determinar a saída
        return 1 if total > self.threshold else 0

    def train(self, training_inputs, labels, epochs):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                # Ajusta os pesos e o limiar
                self.weights = [w + self.learning_rate * error * i for w, i in zip(self.weights, inputs)]
                self.threshold -= self.learning_rate * error
            print(f'{self.weights} and {self.threshold}')
 
# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de dados de treinamento
    training_inputs = [
        [0,0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    labels = [0, 0, 0, 1]  # Saídas esperadas para os exemplos de treinamento

    # Cria o perceptron com 3 entradas
    perceptron = Perceptron(num_inputs=2)

    # Treina o perceptron
    perceptron.train(training_inputs, labels, epochs=10)

    # Testa o perceptron com diferentes entradas após o treinamento
    print(perceptron.predict([1, 0]))  # Bom tempo, sem companhia, longe do transporte
    print(perceptron.predict([0, 1]))  # Tempo ruim, com companhia, perto do transporte
    print(perceptron.predict([1, 1]))  # Bom tempo, com companhia, perto do transporte
