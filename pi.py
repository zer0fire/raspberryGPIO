#coding:utf-8
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json

#BCM GPIO编号
pins = [17, 18, 27, 22, 23, 24, 25, 4]
def gpio_setup():
    #采用BCM编号
    GPIO.setmode(GPIO.BCM)
    #设置所有GPIO为输出状态，且输出低电平
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        
def gpio_destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
        GPIO.setup(pin, GPIO.IN)

#连接并返回成功        
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("gpio")
    
#消息推送和控制GPIO
def on_message(client, userdata, msg):
   print(msg.topic+" "+str(msg.payload))
   gpio = json.loads(str(msg.payload).decode("utf-8"))
   if gpio['pin'] in pins:
      if gpio['value'] == 0:
         GPIO.output(gpio['pin'], GPIO.LOW)
      else:
         GPIO.output(gpio['pin'], GPIO.HIGH)
         
if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    gpio_setup
    
    try:
    #服务器地址根据实际情况可以改变
        client.connect("192.168.0.121", 1882, 60)
        client.loop_forever
    except KeyboardInterrupt:
        client.disconnect()
        gpio_destroy
    