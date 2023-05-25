from temporalio import activity

from model import TransferDetails


@activity.defn(name="withdraw")
async def withdraw(transferDetails: TransferDetails) -> str:
    return f"withdraw {str(transferDetails)}"


@activity.defn(name="withdraw_compensation")
async def withdraw_compensation(transferDetails: TransferDetails) -> str:
    return f"withdraw_compensation {str(transferDetails)}"


@activity.defn(name="deposit")
async def deposit(transferDetails: TransferDetails) -> str:
    return f"deposit {str(transferDetails)}"


@activity.defn(name="deposit_compensation")
async def deposit_compensation(transferDetails: TransferDetails) -> str:
    return f"deposit_compensation {str(transferDetails)}"


@activity.defn(name="step_with_error")
async def step_with_error(transferDetails: TransferDetails) -> str:
    print(f"step_with_error {str(transferDetails)}")

    raise Exception("some error")