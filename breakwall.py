import subprocess

if __name__ == "__main__":
    while (True):
        subprocess.call(['plink','-N','-v','-P','','@suzaku.tk','-D','127.0.0.1:7070','-pw','']);
