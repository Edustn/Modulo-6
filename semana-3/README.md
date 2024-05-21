# Instruções para executar o programa
Nesse arquivo estão contindo informações para executar o arquivo disposto nesse repositório.Este script é responsável pela movimentação do robô, parada e corte do sistema em caso de emergência. Para executar este projeto, siga as etapas abaixo:

1- Certifique-se de que você tenha o ambiente ROS (Robot Operating System) instalado. 

2- Clone este repositório para o seu ambiente local usando o comando `git clone https://github.com/Edustn/Modulo-6.git`. 

3 - Navegue até o diretório `semana-3` do repositório clonado e ative o ambiente virtual. 

4- Instale as dependências listadas no arquivo `requirements.txt` com o comando `pip install -r requirements.txt`.

5- Abra um terminal e execute o comando `ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py` para abrir o Gazebo, que emula o TurtleBot3. 

6- Em outro terminal, seguia esse caminho `semana-3/turtlebot_teleoperado`.

7 - Após isso, execute o comando `python3 main.py` para que haja a execução do script para movimentar o robô.

7- Após seguir esses passos no terminal em que foi executado o arquivo `main.py`, para fazer o robô se movimentar utilize as teclas A,W,D,X; caso necessite que o robô pare porque houve um imprevisto basta teclar S. Entretanto, ocorra algo extremo e precise desconectar o robô para que não se possa enviar mais nenhum comando aperte F.

**Observação**: Estes comandos devem ser executados no terminal Bash para evitar complicações. Seguindo estas etapas, você estará pronto para utilizar o sistema de movimentação, parada e corte do robô em situações de emergência.


Link do vídeo: [https://drive.google.com/file/d/1SeQnRut5FnhbgU1PS0q0izdEHF1YQN-x/view?usp=sharing](https://drive.google.com/file/d/1SeQnRut5FnhbgU1PS0q0izdEHF1YQN-x/view?usp=sharing)

