# Preparando o ambiente ⚠️



Vamos preparar o Raspbian para utilizar este módulo, utilizando pip (Gerenciador de Pacotes do Python). 

Não sabe se possui o pip? Execute o comando abaixo:

**pip –version**

Se for exibido um erro durante a etapa acima, execute o procedimento abaixo para instalar,

**apt-get update && apt-get -f -y  install python-pip**

Vamos verificar o modulo RPi.GPIO e instalar.

**pip search RPi.GPIO**

**pip install RPi.GPIO**

**apt-get install python-dev**

**apt-get install python-dev RPi.GPIO**



# Iremos ver agora as principais funções do RPi.GPIO 

RPi.GPIO.setmode()=>Modo de acesso ao GPIO, BOARD (Posição física dos pinos) 
ou BCM (Numero após GPIO, deve-se tomar cuidado com a revisão da placa pois 
esta informação pode mudar)

RPi.GPIO.setup()=>Configura o pino: (pino e direção [IN ou OUT], 

*exemplo:

RPi.GPIO.setup(12, RPi.GPIO.OUT)

RPi.GPIO.output()=>Configurar como saida: (pino e valor [HIGH ou LOW]), 

*exemplo:

RPi.GPIO.output(12, RPi.GPIO.HIGH)

RPi.GPIO.input()=>Configurar como entrada: (pino) e possui retorno, 

*exemplo:

valor_pino = RPi.GPIO.input(12)

RPi.GPIO.cleanup()=>Restaura para o estado anterior as portas que foram modificadas 
no programa, deve ser a ultima linha antes de finalizar o programa.

exemplo:

**RPi.GPIO.cleanup()**

Ao configurar o setmode() como BOARD ou BCM, a diferença é o número do pino, por exemplo


BOARD   | BCM
------- | ------
11      | GPIO17
12      | GPIO18



Se o setmode() for setado como BOARD, devemos usar o número 11 e 12 em setup().
Se for setado como BCM, devemos usar 17 e 18 em setup().

É importante se atentar neste detalhe para não ter maiores problemas.
