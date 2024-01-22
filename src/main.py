# import click
import function
import report_options
import sys
import os
import re
from datetime import datetime

def print_results_to_file(all_func):
    f = open("output.txt", "w")
    for func in all_func:
        f.write(str(all_func[func]) + "\n")
    f.close()

def parse_ftrace(path, options):
    # file_path = get_full_file_path(path)
    wpp_log = open(options.file_path,"r")
    
    func_entry = [] # stack for function 
    pattern = re.compile(r"(.*)::(.*)\[B_rel\](.*)(::.*)?:(\d+):(.*)") #
    all_func = {}

    for line in wpp_log: # deal wih one line per time
        if line != "\n":
            # (.*)::(.*)\[B_rel\](.*)(::.*)?:(\d+):(.*)
            split_lst = pattern.findall(line) #[('', '', ...)]
            
            if split_lst != []:  
                # print(split_lst)
                if "Entry" in split_lst[0][-1]:
                    func_entry.append((split_lst[0][1], split_lst[0][2]))
                elif "Exit" in split_lst[0][-1]:
                    #pop out a entry function from a non empty stack
                    if func_entry:
                        func_starttime_str, func_name = func_entry.pop()
                        func_starttime_str = func_starttime_str.strip()
                    else:
                        if split_lst[0][2] in all_func:
                            all_func[split_lst[0][2]].empty_entry += 1
                        print("\n")
                        print("Stack is empty, the function call of {} missing entry to match exit".format(split_lst[0][2]))
                        print("\n")
                        continue
                    
                    # check if the entry function match the exit function
                    if split_lst[0][2] == func_name:
                        func_endtime_str = split_lst[0][1].strip()
                        # convert the str time to time object
                        func_starttime = datetime.strptime(func_starttime_str, '%m/%d/%Y-%H:%M:%S.%f')
                        func_endtime = datetime.strptime(func_endtime_str, '%m/%d/%Y-%H:%M:%S.%f')
                        func_total_time = (func_endtime - func_starttime).total_seconds() * 1000

                        if func_name in all_func:
                            # [how many times being called(frequancy), total time(total duration), average duration per call, longest running interval (max duration), least running interval (min duration)]                       
                            func = all_func[func_name]
                            func.frequency += 1
                            func.duration += func_total_time
                            func.dura_per_call = func.duration/func.frequency

                            # [max duration, starttime, endtime]
                            if func_total_time > func.max_duration[0]:
                                func.max_duration[0] = func_total_time # max duration
                                func.max_duration[1] = func_starttime_str # start time of this duration
                                func.max_duration[2] = func_endtime_str # end time of this duration
                            
                            # [min duration, starttime, endtime]
                            if func_total_time <  func.min_duration[0]:
                                func.min_duration[0] = func_total_time # min duration22222
                                func.min_duration[1] = func_starttime_str # start time of this duration
                                func.min_duration[2] = func_endtime_str # end time of this duration
                        
                        else:    
                            max_duration = [func_total_time, func_starttime_str, func_endtime_str] # [max duration, starttime, endtime] 
                            min_duration = [func_total_time, func_starttime_str, func_endtime_str] # [min duration, starttime, endtime] 
                            new_func = function.Function(func_name, func_total_time, func_total_time, max_duration, min_duration)
                            all_func[func_name] = new_func                 
                    else:
                        if split_lst[0][2] in all_func:
                            all_func[split_lst[0][2]].mismatch_entry += 1
                        print("\n")
                        print("oops, Entry function doesn't match Exit function, keep popping from entry stack")
                        print("\n")
        
    wpp_log.close()
    return all_func

def main():
    # get and parse command line arguments
    # expected input is (main.py, file path, print to file[y/n])
    options = report_options.ReportOptions()
    if options.parse_args() == False:
        return None

    all_func = parse_ftrace(options.file_path, options)
    #print("Function Name  |  called frequancy | total call duration | avg call time | max duration --- start time --- endtime | min duration --- start time --- endtime")
    if options.print_to_txt:
        print_results_to_file(all_func)

    # TODO: make a CLI so user can choose between getting function profiling vs errors
        # Also option to print everything
    if options.print_to_term:
        for item in all_func:
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
            print(all_func[item])
            print("\n")
    
    print("ha")

if __name__ == "__main__":
    main()