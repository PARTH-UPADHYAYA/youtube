from cx_Freeze import setup, Executable
base = None    

executables = [Executable("snake.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "PARTH'S SNAKE GAME",
    options = options,
    version = "3.0",
    description = 'THIS GAME OF SNAKE IS ORIGINALLY MADE BY PARTH UPADHYAYA',
    executables = executables
)