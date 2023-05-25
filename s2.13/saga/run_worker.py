import asyncio
from temporalio.client import Client
from temporalio.contrib.opentelemetry import TracingInterceptor
from temporalio.worker import Worker

from model import TransferMoneyTaskQueue
from activities import withdraw, withdraw_compensation, deposit, deposit_compensation
from workflow import TransferMoney


async def main():
    tracer = TracingInterceptor()
    client = await Client.connect("localhost:7233", interceptors=[tracer])

    worker = Worker(
        client,
        task_queue=TransferMoneyTaskQueue,
        workflows=[TransferMoney],
        activities=[withdraw, withdraw_compensation, deposit, deposit_compensation],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())