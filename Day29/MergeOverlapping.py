# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        
        m=[]
        s=-10000
        max=-100000
        
        for i in range(len(intervals)):
            a=intervals[i]
            if a.start>max:
                if i!=0:
                    m.append(Interval(s,max))
                max=a.end
                s=a.start
                
            else:
                if a.end>=max:
                    max=a.end
          # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        
        m=[]
        s=-10000
        max=-100000
        
        for i in range(len(intervals)):
            a=intervals[i]
            if a.start>max:
                if i!=0:
                    m.append(Interval(s,max))
                max=a.end
                s=a.start
                
            else:
                if a.end>=max:
                    max=a.end
        if m==[]:
            m.append(Interval(s,max))
        elif max!=-100000 and m[-1]!=Interval(s,max):
            m.append(Interval(s,max))
        return m
#         Instead of checking all the m it should be at the end only so we can directly compare withe last element
#         if max!=-100000 and Interval(s,max) not in m:
#             m.append(Interval(s,max))
