#if car needs more time, than it car fleet

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target-p)/s for p,s in sorted(zip(position,speed))]
        ans,cur = 0,0
        for t in time[::-1]:
            if t>cur:
                ans+=1
                cur=t
        return ans
