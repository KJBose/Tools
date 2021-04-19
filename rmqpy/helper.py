import logging
import pika
import sys

''' A set of helper functions that may help for future utilities
    with the module.
    -- Mostly functions to collect RabbitMQ usage metrics'''

def total_blocked_channel_count()
    pass
    #blocked_channel_count = pika.channel_number
    # return locked_channel_count

def active_listener_count(channel):
    pass
    #listener_count = channel.listeners
    #return listener_count

def active_sender_count(channel):
    pass
    #sender_count = channel.senders
    #return sender_count

def active_unacked_msg_count(channel):
    pass
    #unacked_msg_count = channel.unacked_msgs
    ''' external '''
    #connection = pika.BlockingConnection()
    #channel = connection.channel()
    #q = channel.queue_declare(q_name)
    #q_len = q.method.message_count
    #return unacked_msg_count

def emit_log(channel):

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'
    channel.basic_publish(
        exchange='direct_logs', routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))
    connection.close()

def recieve_log(channel):

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
        sys.exit(1)

    for severity in severities:
        channel.queue_bind(
            exchange='direct_logs', queue=queue_name, routing_key=severity)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body))

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
