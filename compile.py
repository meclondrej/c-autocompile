import os

extensions: list[str] = [".c", ".h"]
output: str = "a.exe"

todo: list[str] = []
wd: str = os.getcwd()

def ishidden(path: str):
    chr = [char for char in os.path.basename(path)]
    if chr[0] == '.': return True
    return False

def dirloop(dir: str) -> None:
    os.chdir(dir)
    for m in os.listdir("."):
        if ishidden(os.path.abspath(m)):
            continue
        elif os.path.isdir(m):
            dirloop(m)
            os.chdir("..")
        else:
            _, ext = os.path.splitext(m)
            ready: bool = False
            for t in extensions:
                if ext == t:
                    ready = True
                    break
            if ready:
                print("Found: " + os.path.relpath(m, wd))
                todo.append(os.path.relpath(m, wd))

dirloop(".")
os.chdir(wd)
command: str = "gcc "
for i in todo:
    command = command + i + " "
command = command + "-o " + output
print("Executing: " + command)
os.system(command)
