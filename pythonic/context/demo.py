class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

    @staticmethod
    def do_something():
        print("Doing something in the context")


with MyContext() as context:
    context.do_something()
