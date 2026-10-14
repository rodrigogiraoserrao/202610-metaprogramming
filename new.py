_OS = "MacOS"

class Path:
    def __init__(self):
        if _OS == "Windows":
            ...
        else:
            ...

p = Path()
print(p)  # PosixPath

_OS = "Windows"

p2 = Path()
print(p2)  # WindowsPath