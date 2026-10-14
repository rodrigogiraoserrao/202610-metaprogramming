class Path:
    def __init__(self):
        ...


_OS = "MacOS"

p = Path()
print(p)  # PosixPath

_OS = "Windows"

p2 = Path()
print(p2)  # WindowsPath