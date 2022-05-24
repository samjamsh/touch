def create_files(files): 
 for file in files:
  with open(file,"w") as f: f.write("");
import sys as system; arguments = system.argv; arguments_lenght = len(arguments); parameters = arguments[1:]; files = parameters; create_files(files);
