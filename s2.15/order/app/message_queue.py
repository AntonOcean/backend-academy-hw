import pika
from pika.adapters.blocking_connection import BlockingChannel

from .db import session
from .model import Order

# TODO aio-pika
class MQ:
    def __init__(
        self,
        id: str,
        password: str,
        host: str,
        port: int,
    ):
        self.conn = pika.BlockingConnection(
            pika.URLParameters(f'amqp://{id}:{password}@{host}:{port}'),
        )
        self.channel = self.conn.channel()

        self.channel.queue_declare(queue='order_created')
        self.channel.queue_declare(queue='stock_success')
        self.channel.queue_declare(queue='delivery_success')
        self.channel.queue_declare(queue='stock_fail')
        self.channel.queue_declare(queue='delivery_fail')

    def callback(self, ch, method, properties, body: bytes) -> None:
        order_id = body.decode('utf8')
        order = session.query(Order).filter(Order.id == order_id).first()
        order.status = 'complete' if method.routing_key == 'delivery_success' else 'error'
        session.add(order)
        session.commit()
        print('[*] Transaction end')

    def consume(self, queue: str) -> None:
        self.channel.basic_consume(
            on_message_callback=self.callback,
            queue=queue,
            auto_ack=True,
        )
        self.channel.start_consuming()

    def produce(self, exchange: str, routing_key: str, body: str) -> None:
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body,
        )

    def close(self):
        self.conn.close()
