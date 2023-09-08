"""
    Jordan Wheeler
    7 September 2023
    Module 3    
    This program sends a message to a queue on the RabbitMQ server.

"""

# add imports at the beginning of the file
import pika

# Define a messsage to send

MESSAGE = ["Hello World!", "How are you?", "I am fine, thank you for asking.", "Now we know how to send messages to a queue"]
# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue="hello")

# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=f'{MESSAGE[0]}')
ch.basic_publish(exchange="", routing_key="hello", body=f'{MESSAGE[1]}')
ch.basic_publish(exchange="", routing_key="hello", body=f'{MESSAGE[2]}')
ch.basic_publish(exchange="", routing_key="hello", body=f'{MESSAGE[3]}')

# print a message to the console for the user
print(f" [x] Sent: {MESSAGE [0]}")
print(f" [x] Sent: {MESSAGE [1]}")
print(f" [x] Sent: {MESSAGE [2]}")
print(f" [x] Sent: {MESSAGE [3]}")


# close the connection to the server
conn.close()
