from cx_Freeze import setup, Executable

base = None

executables = [Executable("Guess_The_Number_Game.py", base=base)]

packages = ["idna","random","os"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Guess_The_Number_Game",
    options = options,
    version = "1.0",
    description = 'You have to Guess a number which lies between 1 to 100 both inclusive in minimum Possible moves.',
    executables = executables
)
