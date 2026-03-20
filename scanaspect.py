import os
import subprocess
import time
from datetime import datetime

VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"

suspect_apps = [
"shizuku",
"mt",
"parallel",
"virtual",
"mod",
"cheat",
"lucky",
"patcher"
]

suspect_files = [
".lua",
".sh",
"mod",
"hack",
"script"
]

apps_found = 0
files_found = 0
