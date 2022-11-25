import os

missingLibrary = False
print("Verifying required libraries...")
try:
  from art import *
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("pip install -U art")
  print("Done!")


try:
  import readline
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("pip install -U readline")
  print("Done!")


try:
  from scapy.all import *
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("pip install scapy")
  print("Done!")

print("Adding GhostArp to path")
os.system("mkdir /usr/lib/GhostArp")
os.system("cp -r * /usr/lib/GhostArp")
os.system("cp -r bin/ghostarp /usr/bin/")
os.system("chmod +x /usr/bin/ghostarp")

if missingLibrary:
  print("Restarting to refresh content...")
  import main
  exit()
