from src.Application import Application
import os
import sys

print("User Current Version:-", sys.version)

if __name__ == "__main__":
    os.chdir("../")
    Application().run()


