import sys

import os
import time

print("==============================")
print("-OPERATING SYSTEMS LABORATORY-")
print("-PROCESS MONITORING ACTIVITY-")
print(sys.version)
print("==============================")

osVar = os.getpid()

print("Process ID (PID):", osVar)
print("Process has been created")
print("Process is executing...\n")

for i in range(1, 16):
    print("Execution step: ", i)
    time.sleep(2)

print("Process execution completed.")
print("Process is terminating")