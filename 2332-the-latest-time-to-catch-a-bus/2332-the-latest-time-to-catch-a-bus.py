class Solution:
    def latestTimeCatchTheBus(self, bus: List[int], pas: List[int], cap: int) -> int:
        bus.sort()
        pas.sort()
        p = 0
        for i in range(len(bus)): 
            curr = 0
            while p < len(pas) and pas[p] <= bus[i] and curr < cap:
                curr += 1
                p += 1
            # just process when last
            # cuz the quest ask for max time
            if i == len(bus) - 1:
                if curr < cap: # bus not full
                    t = bus[i] # so try from last time des buss
                    # k以遍历乘客,以寻可'插空'者
                    # t递减,若无空则k之时仍同t,否则得空矣!
                    k = p - 1
                    # tricky one causing the greedy:
                    # 纵使 '我比较的对象上了上辆车'
                    # 仍叵取值，以 '时叵同'
                    while k >= 0 and pas[k] == t:
                        k -= 1
                        t -= 1
                    return t
                else: #  bus is full
                    t = pas[p - 1] - 1 # try before last person
                    k = p - 2
                    while k >= 0 and pas[k] == t:
                        k -= 1
                        t -= 1
                    return t
                    
            
        return 404
    
        # if q == 0:
        #     tar = bus[-1]
        #     while tar in pas:
        #         tar -= 1
        #     return tar
        # else:
        #     if curr == cap:
        #         tar = pas[p - 1] - 1 
        #         while tar in pas:
        #             tar -= 1
        #         return tar
        #     else:
        #         return pas[p - 1] + 1