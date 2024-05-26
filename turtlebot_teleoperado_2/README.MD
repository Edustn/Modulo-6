# Instruções para executar o programa
Nesse arquivo estão contindo informações para executar o arquivo disposto nesse repositório.Este script é responsável pela movimentação do robô, parada e corte do sistema em caso de emergência.Também é possível esse repositório obsservar as imagens que o robô está vendo durante o percurso. Para executar este projeto na parte de movimentação do robô, siga as etapas abaixo:

1- Certifique-se de que você tenha o ambiente ROS (Robot Operating System) instalado. 

2- Clone este repositório para o seu ambiente local usando o comando `git clone https://github.com/Edustn/Modulo-6.git`. 

3 - Navegue até o diretório `semana-3` do repositório clonado e ative o ambiente virtual. 

4- Instale as dependências listadas no arquivo `requirements.txt` com o comando `pip install -r requirements.txt`.

5- Abra um terminal e execute o comando `ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py` para abrir o Gazebo, que emula o TurtleBot3. 

6- Em outro terminal, seguia esse caminho `semana-3/turtlebot_teleoperado`.

7 - Após isso, execute o comando `python3 main.py` para que haja a execução do script para movimentar o robô.

8- Após seguir esses passos no terminal em que foi executado o arquivo `main.py`, para fazer o robô se movimentar utilize as teclas A,W,D,X; caso necessite que o robô pare porque houve um imprevisto basta teclar S. Entretanto, ocorra algo extremo e precise desconectar o robô para que não se possa enviar mais nenhum comando aperte F.


**Observação**: Estes comandos devem ser executados no terminal Bash para evitar complicações. Seguindo estas etapas, você estará pronto para utilizar o sistema de movimentação, parada e corte do robô em situações de emergência.

Passos para observar as imagens da percurso do robô:

1 - Acesse seu TurtleBot3 por SSH, após isso crie um arquivo chamado `sender.py`. Com a criação desse arquivo volte para seu computador que não está conectado pelo SSH e copie as linhas do `sender.py` depositado nas pasta do repositório clonado e volte para o teminal conecado pelo SSH e cole esse código no arquivo `sender.py`.

2 - Depois disso, garnta que seu TurtleBot3 tenha o RosBridge instalado e entaão execute `ros2 launch rosbridge_server rosbridge_websocket_launch.xml`

2 - Após isso, execute no terminal conectado conm SSH `python3 sender.py` e volte para o seu ambiente de execução que não está com ssh.

3 - Agora volte para o diretório `turtlebot_teleoperado_2`e abara o arquivo imagens.html no navegador Chrome. 


Link do vídeo: 
