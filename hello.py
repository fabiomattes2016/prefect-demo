from prefect import flow
from tasks.string_block import create_message


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
    
if __name__ == "main":
    hello_world()