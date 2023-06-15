# python code to create Linux user
import subprocess

userName = input("Enter user-name to create: ")
if len(userName) > 1:
    p1 = subprocess.run(["sudo", "useradd", userName.lower()],capture_output=True, text=True)
    if p1.returncode != 0:
        print(p1.stderr)
    else:
        print("user created!!!")
        print()
        print("tailing passwd file...")
        subprocess.run(["tail", "-1", "/etc/passwd"])
else:
    print("no data entered!!!")