import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BOARD)
print “ Configurando o modo de acesso ao GPIO - BOARD”
print


gpio.setup(11, gpio.OUT)
print “Setando modo OUTPUT no PINO11 GPIO17 [LED VERDE]”

gpio.setup(12, gpio.OUT)
print “Setando modo OUTPUT no PINO12 GPIO18 [LED VERMELHO]”
print

gpio.output(11, gpio.HIGH)
print “Led Verde aceso!”
time.sleep(2)

gpio.output(11, gpio.LOW)
print “Led Verde apagado!”
time.sleep(2)

print

gpio.output(12, gpio.HIGH)
print “Led Vermelho aceso!”
time.sleep(2)

gpio.output(12, gpio.LOW)
print “Led Vermelho apagado!”
time.sleep(2)


gpio.cleanup()
