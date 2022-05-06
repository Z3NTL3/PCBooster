import pathlib
import shutil

def Cleaner():
	dirToRemove = "AppData\\Local\\Temp"
	homedirectory = pathlib.Path.home()
	directory = f"{homedirectory}\\{dirToRemove}"

	shutil.rmtree(directory,True)

if __name__ == "__main__":
	Cleaner()
