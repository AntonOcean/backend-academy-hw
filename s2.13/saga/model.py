from typing import NamedTuple

TransferMoneyTaskQueue = "TRANSFER_MONEY_TASK_QUEUE"

TransferDetails = NamedTuple("TransferDetails", [
    ("amount", float), ("fromAccount", str), ("toAccount", str), ("referenceID", str)])


if __name__ == '__main__':
    tr = TransferDetails(amount=10.1, fromAccount="", toAccount="", referenceID="")
    print(tr.amount)