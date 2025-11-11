class Sample:
    def __init__(self, ola: str):
        print(ola)

    def __enter__(self):
        return "abc"

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exit")


sample = Sample(ola="OI")

with Sample(ola="OI") as s:
    print("Context")
