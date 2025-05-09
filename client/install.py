import subprocess

with open("modlist.txt") as file:
    for line in file:
        subprocess.run(["packwiz", "modrinth", "install", f"\"{line}\""])
