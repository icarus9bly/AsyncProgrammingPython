from tasks import my_intensive_function
result = my_intensive_function.delay("Hawaldaar")
result.get()
