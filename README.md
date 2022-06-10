# AsyncProgrammingPython
- [Async IO in Python](https://realpython.com/async-io-python/)
- [What Is the Python Global Interpreter Lock (GIL)](https://realpython.com/python-gil/#what-problem-did-the-gil-solve-for-python)

# AsyncIO
- await should always be inside a coroutine aka async function.
- To run a coroutine we must at it to event loop in one of these 2 ways:
  - await the coroutine
  - create task

# Celery - Distributed Task Queue
- [Celery parallel distributed task with multiprocessing](https://stackoverflow.com/questions/23916413/celery-parallel-distributed-task-with-multiprocessing)
- Task queues are used as a mechanism to distribute work across threads or machines.