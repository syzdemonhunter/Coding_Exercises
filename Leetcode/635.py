# https://leetcode.com/problems/design-log-storage-system/

# Because the number of operations is very small, we do not need a complicated structure to store the logs: a simple list will do.

# Let's focus on the retrieve function. For each granularity, we should consider all timestamps to be truncated to that granularity. For example, if the granularity is 'Day', we should truncate the timestamp '2017:07:02:08:30:12' to be '2017:07:02'. Now for each log, if the truncated timetuple cur is between start and end, then we should add the id of that log into our answer.

class LogSystem:

    def __init__(self):
        self.logs = []
        

    def put(self, tid: int, timestamp: str) -> None:
        self.logs.append((tid, timestamp))
        

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        idx_dict = {'Year': 5, 'Month': 8, 'Day': 11, 
                 'Hour': 14, 'Minute': 17, 'Second': 20}
        idx = idx_dict[gra]
        start = s[:idx]
        end = e[:idx]
        
        return sorted(tid for tid, timestamp in self.logs 
                      if start <= timestamp[:idx] <= end)
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)