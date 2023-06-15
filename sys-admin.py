# import os
# os.system("ls -l")

import subprocess
# subprocess.run(["ls","-l"])
# print()
# subprocess.run(["ls","-l","README.md"])

# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

# command="ps"
# commandArgument="-x"
# print(f'Gathering active process information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

#res = subprocess.run(["grep","ec2-user","/etc/passwd"])
#print(res.stdout)
s = subprocess.check_output(["echo", "Hello World!"])

print(s)