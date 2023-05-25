import asyncio
import uuid

from temporalio.client import Client
from temporalio.contrib.opentelemetry import TracingInterceptor

from model import TransferMoneyTaskQueue, TransferDetails
from workflow import TransferMoney

tracer = TracingInterceptor()
client = await Client.connect("localhost:7233", interceptors=[tracer])


async def main():
    td = TransferDetails(amount=54.99, fromAccount="001-001", toAccount="002-002", referenceID=uuid.uuid4().hex)

    result = await client.execute_workflow(TransferMoney.run, td, id="transfer-money-workflow", task_queue=TransferMoneyTaskQueue)

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())