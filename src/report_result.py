from util import parse_wpp_util
import report_options

class ReportResult():
    def __init__(self, options):
        if options.get_errors:
            self.ewi = parse_wpp_util.parse_ewi(options.file_path)
        else:
            self.ewi = {}

        if options.get_func_prof:
            self.all_func = parse_wpp_util.parse_ftrace(options.file_path)
        else:
            self.all_func = []


    def parse_log(self, filename):
        self.ewi = parse_wpp_util.parse_ewi(filename)
        ewi_op = open("ewi_op.txt", "w")
        for key in self.ewi:
            ewi_op.write(key + ": \n")
            for val in self.ewi[key]:
                ewi_op.write("- " + str(val) + "\n")
        ewi_op.close()

    def get_report(options):
        # run ewi parser
        # get ewi summary
        # run function tracer
        return
    
    def print_report(self, options):
        if self.ewi:
            ewi_op = open("ewi_op.txt", "w")
            # summary
            ewi_op.write("SUMMARY\n")
            for key in self.ewi:
                ewi_op.write(key + ": " + str(len(self.ewi[key])) + "\n")

            # detailed o/p
            ewi_op.write("\nVERBOSE\n")
            for key in self.ewi:
                ewi_op.write(key + ": \n")
                for val in self.ewi[key]:
                    ewi_op.write("- " + val[0].strip() + ": " + val[1].strip() + "\n")
            ewi_op.close()

        if self.all_func:
            f = open("output.txt", "w")
            for func in self.all_func:
                f.write(str(self.all_func[func]) + "\n")
            f.close()

        return
