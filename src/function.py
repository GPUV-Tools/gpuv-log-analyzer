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