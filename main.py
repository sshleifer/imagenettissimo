import subprocess

def main():
    with open("params.txt") as f:
        lines = f.readlines()
        for argv in lines:
            if (argv.startswith("#")): continue
            subprocess.run(['python', 'train_imagenette.py'] + argv.rstrip().split())

if __name__ == "__main__":
    main()
