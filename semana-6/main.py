import numpy as np

class MLP:
    def __init__(self, num_inputs, num_hidden, num_outputs, learning_rate=0.1):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs
        self.learning_rate = learning_rate

        # Aqui esta havendo a inicializacao dos pesos
        self.weights_input_hidden = np.random.rand(self.num_inputs, self.num_hidden)
        self.weights_hidden_output = np.random.rand(self.num_hidden, self.num_outputs)
        
        # Aqui esta havendo a inicializacao dos bies do modelo
        self.bias_hidden = np.random.rand(self.num_hidden)
        self.bias_output = np.random.rand(self.num_outputs)

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def _sigmoid_derivative(self, x):
        return x * (1 - x)

    def _mse(self, predictions, targets):
        return np.mean((predictions - targets) ** 2)

    def forward_pass(self, inputs):
        # Hidden layer
        self.hidden_layer_activation = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = self._sigmoid(self.hidden_layer_activation)
        
        # Output layer
        self.output_layer_activation = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output = self._sigmoid(self.output_layer_activation)
        
        return self.output

    def train(self, training_inputs, labels, epochs=7000):
        for epoch in range(epochs):
            for inputs, label in zip(training_inputs, labels):
               
                output = self.forward_pass(inputs)
                
                # Calculo do erro do modelo 
                error = label - output
                
                # Parte faz que faz o gradiente
                d_output = error * self._sigmoid_derivative(output)
                
                # Camada escondida
                error_hidden_layer = d_output.dot(self.weights_hidden_output.T)
                d_hidden_layer = error_hidden_layer * self._sigmoid_derivative(self.hidden_layer_output)
                
                # Atualizacao dos pesos e dos bais conforme se deu o calculo do gradiente
                self.weights_hidden_output += self.hidden_layer_output[:, np.newaxis].dot(d_output[np.newaxis, :]) * self.learning_rate
                self.bias_output += d_output * self.learning_rate

                self.weights_input_hidden += np.array(inputs)[:, np.newaxis].dot(d_hidden_layer[np.newaxis, :]) * self.learning_rate
                self.bias_hidden += d_hidden_layer * self.learning_rate

            if epoch % 1000 == 0:
                predictions, _ = self.predict(training_inputs)
                mse = self._mse(predictions, labels)
                print(f'Epoch: {epoch}, MSE: {mse}')

    def predict(self, inputs):
        predictions = []
        binary_predictions = []
        for inp in inputs:
            output = self.forward_pass(inp)
            predictions.append(output)
            binary_predictions.append(1 if output >= 0.5 else 0)
        return np.array(predictions), np.array(binary_predictions)

def main():
    training_inputs = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    
    labels = np.array([
        [0],
        [1],
        [1],
        [0]
    ])
    
    mlp = MLP(num_inputs=2, num_hidden=2, num_outputs=1)
    mlp.train(training_inputs, labels)
    
    predictions, binary_predictions = mlp.predict(training_inputs)
    mse = mlp._mse(predictions, labels)
    print(f'Final MSE: {mse}')
    print('Predictions (continuous):')
    print(predictions)
    print('Resultado da predicao:')
    print(binary_predictions)

if __name__ == "__main__":
    main()
