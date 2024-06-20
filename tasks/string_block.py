from prefect import task
from prefect.blocks.system import String


@task
def create_message():
    print("New version")
    string_block = String.load("test-string")
    msg = string_block.value
    return msg