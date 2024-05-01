Aqui está contido um projeto que busca realizar um desenho a partir de um script criado. Sendo assim, para experimentar o projeto de desenho com o TurtleSim, siga estas etapas simples:

**Ateção**: Alguns dos comandos descritos para executar a instalação de algumas dependências e afins serão executados utilizando o bash. Portanto, certifique-se de estar utilizando o bash para realizar os passos corretamente.

1. Clone o repositório: Primeiro, clone ou baixe o repositório do projeto do TurtleSim  [https://github.com/Edustn/Modulo-6/tree/main/semana-1/turtlesim](https://github.com/Edustn/Modulo-6/tree/main/semana-1/turtlesim)

2. Ative o ambiente virtual Python. Ative-o usando o seguinte comando: `source my_env/bin/activate`

Substitua my_env pelo nome do seu ambiente virtual.

3. Instale as dependências: Navegue até o diretório do projeto e instale as dependências listadas no arquivo requirements.txt com o seguinte comando: `pip install -r requirements.txt`

4. Construa o projeto: Na raiz do projeto, execute o seguinte comando para baixar e construir os pacotes necessários: `colcon build` 

5. Execute o TurtleSim: Abra um terminal e execute o TurtleSim com o seguinte comando: `ros2 run turtlesim turtlesim_node`

Isso abrirá a tela do TurtleSim com uma tartaruga.

6. Execute o script do projeto: Em outro terminal, navegue até o diretório do projeto e execute o script responsável por enviar comandos para o desenho da tartaruga e manipulá-la. Use o seguinte comando: `ros2 run ola_mundo ola`

Isso iniciará a sequência de desenhos da tartaruga, seguida pelo aparecimento de uma nova tartaruga e, eventualmente, a morte dela após um determinado tempo.
