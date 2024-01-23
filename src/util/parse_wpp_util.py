import report_result
import util.time_summary as time_summary
import function
import re

# input: the full wpp log
# output: a dictionary containing info, warning, and error messages
def parse_ewi(file_path: str) -> dict[str, list[tuple[str, str]]]:
    log = open(file_path, "r")
    ewi = {}
    pattern = re.compile(r"(.*)::(.*)\[B_rel\](gim.*libgv):.*(\[.*)")
    for line in log:
        if line != "\n":
            split_list = pattern.findall(line)
            if split_list != []:
                _, log_time, log_type, log_msg = split_list[0]
                val = (log_time, log_msg)
                if log_type not in ewi:
                    ewi[log_type] = [val]
                else:
                    ewi[log_type].append(val)
    log.close()
    return dict(sorted(ewi.items()))

def get_ewi_summary(ewi: dict[str, list[str]]):
    ewi_summary = {}

    return

def parse_ftrace(file_path):
    wpp_log = open(file_path,"r")
    
    func_entry = [] # stack for function 
    pattern = re.compile(r"(.*)::(.*)\[B_rel\](.*)(::.*)?:(\d+):(.*)") #
    all_func = {}

    for line in wpp_log: # deal wih one line per time
        if line != "\n":
            split_list = pattern.findall(line) #[('', '', ...)]
            
            if split_list != []:     
                if "Entry" in split_list[0][-1]:
                    func_entry.append((split_list[0][1], split_list[0][2]))
                elif "Exit" in split_list[0][-1]:
                    #pop out a entry function from a non empty stack
                    if func_entry:
                        func_starttime_str, func_name = func_entry.pop()
                        func_starttime_str = func_starttime_str.strip()
                    else:
                        if split_list[0][2] in all_func:
                            all_func[split_list[0][2]].empty_entry += 1
                        # print("\n")
                        # print("Stack is empty, the function call of {} missing entry to match exit".format(split_list[0][2]))
                        # print("\n")
                        continue
                    
                    # check if the entry function match the exit function
                    if split_list[0][2] == func_name:
                        func_endtime_str = split_list[0][1].strip()
                        func_time = time_summary.TimeSummary(func_starttime_str, func_endtime_str)

                        if func_name in all_func:
                            # [how many times being called (frequency), total time (total duration), average duration per call, longest running interval (max duration), least running interval (min duration)]                       
                            func = all_func[func_name]
                            func.frequency += 1
                            func.duration += func_time.total_time
                            func.dura_per_call = func.duration / func.frequency
                            func.max_duration = func_time if func_time.total_time > func.max_duration.total_time else func.max_duration
                            func.min_duration = func_time if func_time.total_time < func.max_duration.total_time else func.min_duration
                        else:
                            new_func = function.Function(func_name, func_time.total_time, func_time.total_time, func_time, func_time)
                            all_func[func_name] = new_func                 
                    else:
                        if split_list[0][2] in all_func:
                            all_func[split_list[0][2]].mismatch_entry += 1
                        # print("\n")
                        # print("oops, Entry function doesn't match Exit function, keep popping from entry stack")
                        # print("\n")
        
    wpp_log.close()
    return all_func