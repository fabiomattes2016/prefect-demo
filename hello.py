from prefect import flow, task
from prefect.blocks.system import String

@task
def create_message():
    string_block = String.load("test-string")
    msg = string_block.value
    return msg

@flow
def something_else():
    result = 10
    return(result)

@flow
def hello_world():
    subflow_message = something_else()
    task_message = create_message()
    new_message = task_message + str(subflow_message)
    print(new_message)
    
# if __name__ == "main":
hello_world()