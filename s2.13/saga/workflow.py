from datetime import timedelta
from temporalio import workflow
from temporalio.client import WorkflowFailureError
from temporalio.common import RetryPolicy

from model import TransferDetails


@workflow.defn
class TransferMoney:
    @workflow.run
    async def run(self, transferDetails: TransferDetails):
        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=1),
            backoff_coefficient=2.0,
            maximum_interval=timedelta(minutes=1),
            maximum_attempts=3
        )

        try:
            result = await workflow.execute_activity(
                "withdraw", transferDetails, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy
            )
            print(result)
        except WorkflowFailureError as err:
            result = await workflow.execute_activity(
                "withdraw_compensation", transferDetails, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy
            )
            print(result)

        try:
            result = await workflow.execute_activity(
                "deposit", transferDetails, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy
            )
            print(result)
        except WorkflowFailureError as err:
            result = await workflow.execute_activity(
                "deposit_compensation", transferDetails, start_to_close_timeout=timedelta(seconds=5), retry_policy=retry_policy
            )
            print(result)