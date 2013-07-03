import subprocess

if __name__ == "__main__":
    while (True):
        subprocess.call(['ssh','-qTnN','-D','7070','waldronluo@suzaku.tk']);
