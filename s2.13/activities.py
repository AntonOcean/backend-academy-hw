import time

from temporalio import activity

# save to DB
# go to payment system
# go external service API
# worker - calc
@activity.defn(name="python-course")
async def say_hello(name: str) -> str:
    # raise Exception
    return f"Hello, {name}!"