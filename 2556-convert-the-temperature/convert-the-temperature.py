class Solution(object):
    def convertTemperature(self, celsius):
        ans = [celsius + 273.15, (celsius * 1.8) + 32]
        return ans
       
        