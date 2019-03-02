def deprecated(message):
    def wrapper(func):
        if message is not None:
            print(message)
    
    return wrapper