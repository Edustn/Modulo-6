import torch
import torch.nn as nn
import torch.optim as optim

inputs = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
outputs = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

class XORModel(nn.Module):
    def __init__(self):
        super(XORModel, self).__init__()
        self.layer1 = nn.Linear(2, 2)  # 2 entradas, 2 neurônios na camada oculta
        self.layer2 = nn.Linear(2, 1)  # 2 neurônios na camada oculta, 1 saída

    def forward(self, x):
        x = torch.sigmoid(self.layer1(x))
        x = torch.sigmoid(self.layer2(x))
        return x

model = XORModel()

# Definir a função de perda e o otimizador
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

epochs = 30000  

for epoch in range(epochs):
    y_pred = model(inputs)
    # Calcular a perda
    loss = criterion(y_pred, outputs)
    optimizer.zero_grad()
    loss.backward()
    # Atualizar os pesos
    optimizer.step()
    
    if (epoch + 1) % 1000 == 0:
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')

# Fazer predições

print("Resultados da predição:")
predictions = model(inputs)
predictions = predictions.round()  
predictions = predictions.int()

for i in predictions:
    print(i.numpy())


# video de referencia para implementacao: https://www.youtube.com/watch?v=3I_66lyFOqI