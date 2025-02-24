import json

# some JSON:
llnJSON =  '{"Hiroki":"08078", "Noah":"08044", "Tygo":"08153", "Esther":"08060"}'

# parse x:
llnPy = json.loads(llnJSON)

#input test

name = input("Enter name:")

# the result is a Python dictionary:
print(llnPy[name]) 