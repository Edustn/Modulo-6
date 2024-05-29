# Instruções para executar o programa
Nesse arquivo estão contindo informações para executar o arquivo disposto nesse repositório.Este script é responsável pela movimentação do robô e parada em caso de emergência.Também nesse repositório  é possível observar imagens que estão sendo transmitidas pela webcam em tempo real. Para executar este projeto na parte de movimentação do robô, siga as etapas abaixo:

1 - Certifique-se de que você tenha o ambiente ROS (Robot Operating System) instalado.

2 - Clone este repositório para o seu ambiente local usando o comando `git clone https://github.com/Edustn/Modulo-6.git`.

3 - Navegue até o diretório semana-3 do repositório clonado e ative o ambiente virtual.

4 - Instale as dependências listadas no arquivo `requirements.txt` com o comando `pip install -r requirements.txt`.

5 - Abra um terminal e execute o comando `ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py` para abrir o Gazebo, que emula o TurtleBot3.

6 - Garanta que você tenha o RosBridge instalado. Caso não tenha, execute o comando: `sudo apt install ros-humble-rosbridge-suite`. Caso já esteja instalado, execute o comando: `ros2 launch rosbridge_server rosbridge_websocket_launch.xml`.

7 - Em outro terminal, vá para o diretório `turtlebot_teleoperado_2`.

8 - Após isso, execute no terminal `python3 sender.py`.

9 - Depois, abra o arquivo imagens.html no Chrome e comece a utilizar o programa desenvolvido com as teclas A, W, S, X ou pelos botões dispostos na interface.

**Observação**: Estes comandos devem ser executados no terminal Bash para evitar complicações. Seguindo estas etapas, você estará pronto para utilizar o sistema de movimentação, parada e corte do robô em situações de emergência.

Link do vídeo: [https://drive.google.com/file/d/1WM9ss2v02gHqkbn0tuF7MJ_NCspXgoMw/view?usp=sharing](https://drive.google.com/file/d/1WM9ss2v02gHqkbn0tuF7MJ_NCspXgoMw/view?usp=sharing)
