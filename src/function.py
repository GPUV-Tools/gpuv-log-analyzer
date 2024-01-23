class Function:
    def __init__(self, name, duration, dpc, max_dura, min_dura) -> None:
        self.name = name
        self.frequency = 1
        self.duration = duration
        self.dura_per_call = dpc
        self.max_duration = max_dura
        self.min_duration = min_dura
        self.empty_entry = 0
        self.mismatch_entry = 0
    
    def __str__(self) -> str:     
        str = """
        Function name: {}
        Frequency: {}
        Total duration: {}ms
        Avg duration per call: {}ms
        Max duration:
            total time: {}ms
            start time: {}
            end time: {}
        Min duration:
            total time: {}ms
            start time: {}
            end time: {}
        Num of empty stack error: {}
        Num of function's entry and exit mismatch: {}
        """.format(
            self.name,
            self.frequency,
            self.duration,
            self.dura_per_call,
            self.max_duration.total_time,
            self.max_duration.start_time,
            self.max_duration.end_time,
            self.min_duration.total_time,
            self.min_duration.start_time,
            self.min_duration.end_time,
            self.empty_entry,
            self.mismatch_entry)
        return str