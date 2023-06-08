from .message_queue import MQ


def job_delivery_success():
    print("Hello job delivery_success")

    mq = MQ(
        id='admin',
        password='admin',
        host='127.0.0.1',
        port=5672,
    )
    mq.consume(queue='delivery_success')
    mq.close()

    print("Bye job")


def job_stock_fail():
    print("Hello job stock_fail")

    mq = MQ(
        id='admin',
        password='admin',
        host='127.0.0.1',
        port=5672,
    )
    mq.consume(queue='stock_fail')
    mq.close()

    print("Bye job")