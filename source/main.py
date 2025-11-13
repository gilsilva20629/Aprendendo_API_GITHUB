import subprocess

run_server = ["python3", "server.py"]
#ls = ["ls", "-la"]


result = subprocess.run(run_server, capture_output=True, text=True)
#result = subprocess.run(ls, capture_output=True, text=True, encoding="utf-8", timeout=10)
#result = subprocess.run(run_server, capture_output=True, text=True, encoding="utf-8", timeout=10, check=True)

print(result.returncode, "\n", result.stdout)



'''
try:
	result = subprocess(run_server, capture_output=True, text=True, encoding="utf-8", timeout=10, check=True)
	#print(result.check_returncode)
	print(result.stdout)
	
except Exception as err:
	print(err, type(err))
	print("stderr", result.stderr)
#except subprocess.SubprocessError as sb_err :
#except subprocess.CalledProcessError as cp_err :
#except subprocess.TimeoutExpired as te_err :
finally:
	print("pronto")
'''