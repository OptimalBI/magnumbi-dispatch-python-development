# Python - MagnumBI Dispatch Client Development Repository.

MagnumBI Dispatch manages microservice communication and interaction simply.   
It is easy to develop and integrate with your small to medium sized development teams.

This is the repository for developing the python client library.  
If you just wish to use the client library see [this repository](../magnumbi-dispatch-python-library)

## Requirements

Python 3.3 or greater. Python 2.x not supported.

## Getting started

Clone this project and edit magnumbi_depot.DispatchClient to start.  
 See the example below for more details.

PyPI coming soon!

## Examples

```python
import magnumbi_depot

client = magnumbi_depot.DispatchClient(
    uri='127.0.0.1',
    port=6883,
    access_key='test',
    secret_key='token',
    ssl_verify=False
)

status_result = client.check_status() # Will return True if connection to the server functioned correctly.
```