# Modules.
from os import popen

# Variables.
modules_list = popen('pip freeze')
data = modules_list.read().split('\n')
data.remove('')
data_len = len(data)

# Loop to uninstall each name.
for x in range(data_len):
    log = popen('pip uninstall {} -y'.format(data[x]))
    output = log.read()
    print(output)