#!/usr/bin/python3
import subprocess
import sys

def check_platform():
	if sys.platform == 'win32':
		print("Windows is not supported now!")
		sys.exit(1)
	else:
		pass

def os_name():
	global name
	output = subprocess.check_output(["lsb_release", "-a"]).decode("utf-8")
	name = output.split("\n")[1].split("\t")[1]

def processor_model():
	global proc_model
	output = subprocess.check_output('lscpu')
	output = output.split()
	vendor = output[47]
	model = output[48]
	code = output[49]
	vendor = str(vendor)
	model = str(model)
	code = str(code)
	vendor = vendor.split("'")[1]
	model = model.split("'")[1]
	code = code.split("'")[1]
	proc_model = vendor, model, code

def cpu_max_mhz():
	global max_frequency
	output = subprocess.check_output('lscpu')
	output = output.split()[61]
	output = str(output)
	output = output.split("'")[1]
	max_frequency = output, "MHz"

def cpu_min_mhz():
	global min_frequency
	output = subprocess.check_output('lscpu')
	output = output.split()[65]
	output = str(output)
	output = output.split("'")[1]
	min_frequency = output, "MHz"

def architecture():
	global arch
	output = subprocess.check_output('lscpu')
	output = str(output.split()[1])
	arch = output.split("'")[1]

def num_cores():
	global cores
	output = subprocess.check_output('lscpu')
	cores = output.decode("utf-8").split()[31]

def num_threads():
	global threads
	output = subprocess.check_output('lscpu')
	threads = output.decode("utf-8").split()[19]

def virtualization():
	global virt
	output = subprocess.check_output('lscpu')
	virt = output.decode("utf-8").split()[69]


check_platform()
os_name()
processor_model()
cpu_max_mhz()
cpu_min_mhz()
architecture()
num_cores()
num_threads()
virtualization()

print("OS Name: \t" + name)
print("Architecture: \t" + arch)
print("Processor: \t" + proc_model[0], proc_model[1], proc_model[2])
print("Cores: \t\t" + cores)
print("Threads: \t" + threads)
print("Max Frequency: \t" + max_frequency[0], max_frequency[1])
print("Min Frequency: \t" + min_frequency[0], min_frequency[1])
print("Virtualization: " + virt)
