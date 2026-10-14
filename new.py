_OS = "MacOS"

class Path:
    def __init__(self):
        ...

def PosixPath(Path):
    ...

def WindowsPath(Path):
    ...

p = Path()
print(p)  # PosixPath

_OS = "Windows"

p2 = Path()
print(p2)  # WindowsPath