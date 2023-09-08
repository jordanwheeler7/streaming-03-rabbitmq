# See Hello World! Example at
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
channel.basic_publish(exchange="", routing_key="hello", body="Your rabbitmq is working!")
channel.basic_publish(exchange="", routing_key="hello", body="Now we will have fun!")
print(" [x] Sent 'Hello World!'")
print(" [x] Sent 'Your RabbitMQ is working!!' ")
print(" [x] Sent 'Now we will have fun!'")
connection.close()
