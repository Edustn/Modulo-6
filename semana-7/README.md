# Comparação de resultados
## Linear:
Treinamento: 79 segundos para 5 épocas

Inferência:  0s 88ms/step

Desempenho: [[7.7173531e-11 1.1808317e-14 3.5739637e-14 1.3339280e-09 5.2503817e-12
  3.0526999e-06 3.7896574e-16 9.9999690e-01 1.5382196e-17 2.7849956e-09]]

## CNN:
Treinamento: 79 segundos para 5 épocas

Inferencia:  0s 56ms/step

Desempenho: [[7.7173531e-11 1.1808317e-14 3.5739637e-14 1.3339280e-09 5.2503817e-12
  3.0526999e-06 3.7896574e-16 9.9999690e-01 1.5382196e-17 2.7849956e-09]]


Com o uso desses dois algorimos pela métricas notamos que o Liner funciona de uma maneira mais rápida do que CNN.

# Explicação das rotas:

A rota `/` é responsável por gerar a primeira interface da aplicação, permitindo selecionar o algoritmo desejado e carregar a imagem para análise.

A rota `/upload` carrega a imagem colocada pelo usuário e devolve no front-end o resultado da análise feita pelo CNN.

A rota `/upload_linear` carrega a imagem colocada pelo usuário e devolve no front-end o resultado da análise feita pelo modelo Linear.

## Como executar o programa:

1. Clone este repositório com o comando: `git clone 'https://github.com/Edustn/Modulo-6.git'`
2. Abra o VS Code e, em seu terminal integrado, navegue até o diretório `semana-7`.
3. Agora vamos começar com o treino dos modelos:
   - `python3 treinamento.py`
   - `python3 treinamento_linear.py`
4. Execute o comando `python3 servidor.py`. Após isso, clique no link gerado para visualizar a aplicação em seu navegador.

**Obs:** Todos os comandos foram dados no ambiente Linux.

Link para o vídeo de tudo funcionando: [https://drive.google.com/file/d/1oSkLTw9TcHoVYiNGHDXKowmUNnpTFYcp/view?usp=sharing](https://drive.google.com/file/d/1oSkLTw9TcHoVYiNGHDXKowmUNnpTFYcp/view?usp=sharing)

