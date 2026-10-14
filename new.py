_OS = "MacOS"

class Path:
    # This is `__init__`'s big brother.
    # `__init__` takes a NEWLY CREATED object and customises it.
    # But it's `__new__` that's actually in charge of CREATING
    # a brand new object.
    def __new__(self...)

class PosixPath(Path):
    ...

class WindowsPath(Path):
    ...

p = Path()
print(p)  # PosixPath

_OS = "Windows"

p2 = Path()
print(p2)  # WindowsPath