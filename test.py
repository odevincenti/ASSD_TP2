# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

from src.Partials import Partials

print("test")

Parciales_Flauta = Partials()

Parciales_Flauta.create_partial("./MATLAB/Parciales_txts/Parciales_Flauta_DO.txt",1)  #1 es flauta ponele




