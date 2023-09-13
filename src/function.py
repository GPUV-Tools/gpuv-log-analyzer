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
        
    # def update_name(self, name) -> None:
    #     self.name = name
    
    # def update_frequency(self, freq) -> None:
    #     self.frequency = freq
    
    # def update_duration(self, duration) -> None:
    #     self.duration = duration
    
    # def update_dura_per_call(self, dpc) -> None:
    #     self.dura_per_call = dpc
    
    # def update_max_duration(self, max_dura) -> None:
    #     self.max_duration = max_dura
    
    # def update_min_duration(self, min_dura) -> None:
    #     self.min_duration = min_dura
    
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
            (self.max_duration)[0],
            (self.max_duration)[1],
            (self.max_duration)[2],
            (self.min_duration)[0],
            (self.min_duration)[1],
            (self.min_duration)[2],
            self.empty_entry,
            self.mismatch_entry)
        return str