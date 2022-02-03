class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        # initially span for first day is 1 
        span = 1
        # if stack is non empty and previous day's price is less than today
        # pop the top price and add that day's span to current day's span
        while self.stack and self.stack[-1][0] <= price: 
            span = span + self.stack.pop()[1] 
        # add current day price and span to the stack
        self.stack.append([price, span]) 
        return span
      
      
      '''
      Problem: https://leetcode.com/problems/online-stock-span/
      
      '''
