import argparse
import os

class ReportOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-file", "--filepath", help = "file name, relative path, or absolute path")
        self.parser.add_argument("-dest", "--destination", help = "report destination: [file, terminal, all]")
        self.parser.add_argument("-fp", "--funcprof", help = "get function profile")
        self.parser.add_argument("-ep", "--errors", help = "get errors")
        self.file_path = ""
        self.print_to_term = False
        self.print_to_txt = False
        self.get_func_prof = True
        self.get_errors = True

    def get_full_file_path(self, path) -> str:
        working_dir = os.getcwd()
        # absolute path provided
        if working_dir in path:
            return path
        # relative path provided
        elif path[0] == "\\":
            return working_dir + path
        # file name provided
        return working_dir + "\\" + path
    
    def set_output_destination(self, dest):
        if dest == "file":
            return [False, True]
        elif dest == "terminal":
            return [True, False]
        elif dest == "all":
            return [True, True]
        return [False, False]

    def parse_args(self) -> bool:
        args = self.parser.parse_args()
        print(args)
        
        self.file_path = self.get_full_file_path(args.filepath)
        if self.file_path == "":
            return False

        self.print_to_term, self.print_to_txt = self.set_output_destination(args.destination)
        if self.print_to_term == False and self.print_to_txt == False:
            return False

        if (args.funcprof != None):
            self.get_func_prof = args.funcproc
        if(args.errors != None):
            self.get_errors = args.errors
        
        return True