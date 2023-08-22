import subprocess

result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))  # Convert bytes to string before printing
