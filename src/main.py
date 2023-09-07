# import click
import re
from datetime import datetime


def main():
    filename = "C:\\Users\\ellapan2\\Desktop\\wpp_example.txt"
    wpp_log = open(filename,"r")
    
    func_entry = []
    pattern = re.compile(r"(.*)::(.*)\[B_rel\](.*)(::.*)?:(\d+):(.*)")
    all_func = {}

    for line in wpp_log: # deal wih one line per time
        if line != "\n":
            # (.*)::(.*)\[B_rel\](.*)(::.*)?:(\d+):(.*)
            split_lst = pattern.findall(line) #[('', '', ...)]
            
            if split_lst != []:  
                if "Entry" in split_lst[0][-1]:
                    func_entry.append((split_lst[0][1], split_lst[0][2]))
                elif "Exit" in split_lst[0][-1]:
                    #pop out a entry function from a non empty stack
                    try:
                        func_starttime, func_name = func_entry.pop()
                        func_starttime = func_starttime.strip()
                    except:
                        print("Stack is empty, there is a lonley function entry that we cannot match, will terminate the program now")
                        break
                    # check if the entry function match the exit function
                    if split_lst[0][2] == func_name:
                        func_endtime = split_lst[0][1].strip()
                        # convert the str time to time object
                        func_starttime = datetime.strptime(func_starttime, '%m/%d/%Y-%H:%M:%S.%f')
                        func_endtime = datetime.strptime(func_endtime, '%m/%d/%Y-%H:%M:%S.%f')
                        func_total_time = func_endtime - func_starttime
                        
                        if func_name in all_func:
                            #[how many times being called(frequancy), total time(duration), average call time, max call duration, min call duration]
                            #{func:[num, num, num, (num, num, num,), (num, num, num)]}
                            func = all_func[func_name]
                            func[0] += 1
                            func[1] += func_total_time
                            func[2] = func[1]/func[0]
                            
                            #(max duration, starttime, endtime)
                            if func_total_time > func[3][0]:
                                func[3][0] = func_total_time
                                func[3][1] = func_starttime
                                func[3][2] = func_endtime
                            
                            #(min duration, starttime, endtime)
                            if func_total_time < func[4][0]:
                                func[4][0] = func_total_time
                                func[4][1] = func_starttime
                                func[4][2] = func_endtime
                        
                        else:                      
                            max_duration = [func_total_time, func_starttime, func_endtime]
                            min_duration = [func_total_time, func_starttime, func_endtime]
                            all_func[func_name] = [1, func_total_time, func_total_time, max_duration, min_duration]
                        
                    else:
                        print("oops, Entry function doesn't match Exit function, keep popping from entry stack")
            else:
                pass
        else:
            pass
        
        
    #print("Function Name                    |  called frequancy | total call duration | avg call time | max duration --- start time --- endtime | min duration --- start time --- endtime")
    for item in all_func:
        print("function name: {}".format(item))
        print(all_func[item])
        print("\n\n")
if __name__ == "__main__":


    main()
    
    
# if r[type] == entry:
#                 s.append(r)
#             elif r[type] == exit and r[func] == s[-1][func] and s[-1][type] == entry
#                 s.pop()

# datetime_str2 = '09/21/2022-9:50:09.181'

# datetime_object2 = datetime.strptime(datetime_str2, '%m/%d/%Y-%H:%M:%S.%f')[:-3]


# a = datetime_object2 - datetime_object1

# print(datetime_object1)  # printed in default format
# print(datetime_object2)  # printed in default format
# print(a)