import report_options
import report_result

def print_results_to_file(all_func):
    f = open("output.txt", "w")
    for func in all_func:
        f.write(str(all_func[func]) + "\n")
    f.close()

def main():
    # get and parse command line arguments
    options = report_options.ReportOptions()
    
    if options.parse_args() == False:
        return None
    
    result = report_result.ReportResult(options)
    result.print_report(options)
    
    # result = report_result.ReportResult()
    # result.parse_log(options.file_path)
    # return None

    # all_func = parse_wpp_util.parse_ftrace(options.file_path)
    #print("Function Name  |  called frequancy | total call duration | avg call time | max duration --- start time --- endtime | min duration --- start time --- endtime")
    # if options.print_to_txt:
    #     print_results_to_file(all_func)

    # TODO: make a CLI so user can choose between getting function profiling vs errors
        # Also option to print everything
    # if options.print_to_term:
    #     for item in all_func:
            # print("Function name: {}".format(all_func[item].name))
            # print("Frequency: {}".format(all_func[item].frequency))
            # print("Total duration: {}ms".format(all_func[item].duration))
            # print("Avg duration per call: {}ms".format(all_func[item].dura_per_call))
            # print("Max duration:")
            # print("    total time: {}ms".format((all_func[item].max_duration)[0]))
            # print("    start time: {}".format((all_func[item].max_duration)[1]))
            # print("    end time: {}".format((all_func[item].max_duration)[2]))
            # print("Min duration:")
            # print("    total time: {}ms".format((all_func[item].min_duration)[0]))
            # print("    start time: {}".format((all_func[item].min_duration)[1]))
            # print("    end time: {}".format((all_func[item].min_duration)[2]))
            # print("Num of empty stack error: {}".format(all_func[item].empty_entry))
            # print("Num of function's entry and exit mismatch: {}".format(all_func[item].mismatch_entry))
            # print(all_func[item])
            # print("\n")
    
    print("ha")

if __name__ == "__main__":
    main()