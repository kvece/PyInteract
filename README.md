# PyInteract
A python library for interacting with subprocesses

## Classes

PyInteract


### Members


#### __init__
Constructor

##### Inputs
| Name    | Required? | Description                          |
| ------- | --------- | ------------------------------------ |
| process | yes       | The name of the process to attach to |
| *args   | no        | Any arguments to pass to the process |


#### interact
Used to for an individual interaction with the process

##### Inputs
| Name    | Required? | Description                          |
| ------- | --------- | ------------------------------------ |
| input   | yes       | The input to send to the process     |
| buffer_timeout   | no        | How long to wait inbetween individual program responses. Default: .1|
| max_timeout   | no        | How long to wait for any program response. Set to 0 to block indefinitely. Default: 0|
| newline   | no        | Add a newline to the end of the input. Default: True|

##### Output
A string containing the result from the process


#### is_alive
Determines whether or not the child process is still alive

##### Output
True if the process is still running

#### status_code
Returns the status code of the process

##### Output
An integer corresponding to the status code
