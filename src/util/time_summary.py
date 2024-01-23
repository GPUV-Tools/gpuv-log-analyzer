from datetime import datetime

class TimeSummary():
    log_timestamp_format ='%m/%d/%Y-%H:%M:%S.%f'
    
    def __init__(self, start_str, end_str):
        self.start_time = start_str
        self.end_time = end_str

        func_starttime = datetime.strptime(start_str, TimeSummary.log_timestamp_format)
        func_endtime = datetime.strptime(end_str, TimeSummary.log_timestamp_format)
        self.total_time = (func_endtime - func_starttime).total_seconds() * 1000

        if self.total_time < 0:
            raise Exception("Start time must be less than end time")