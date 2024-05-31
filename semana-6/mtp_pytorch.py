import torch
import torch.nn as nn
import torch.optim as optim

# Define a MLP class using PyTorch's nn.Module
class MLP(nn.Module):
    def __init__(self, num_input=2, num_hidden=2, num_output=1):
        super(MLP, self).__init__()
        self.hidden = nn.Linear(num_input, num_hidden)
        self.output = nn.Linear(num_hidden, num_output)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.hidden(x))
        x = self.sigmoid(self.output(x))
        return x

# Dados de entrada e saída para a operação XOR
inputs_xor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
targets_xor = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Instancia o modelo, define a função de custo e o otimizador
model = MLP(num_input=2, num_hidden=2, num_output=1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Treinamento do modelo
num_epochs = 10000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(inputs_xor)
    loss = criterion(outputs, targets_xor)
    
    # Backward pass e otimização
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 1000 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Testando a saída após o treinamento
print("Saída após treinamento:")
with torch.no_grad():
    for i in range(len(inputs_xor)):
        output = model(inputs_xor[i])
        print(f"Input: {inputs_xor[i].numpy()}, Predicted Output: {output.item():.4f}")

