def create_files(files):
 for file in files:
  with open(file,"w") as f: f.write("");
import sys as system; help = f'use: {system.argv[0]} filename filename2 ...'; arguments = system.argv; arguments_lenght = len(arguments); system.exit(help) if len(arguments) == 1 else print('',end=''); parameters = arguments[1:]; files = parameters; create_files(files);
