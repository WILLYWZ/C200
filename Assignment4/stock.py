def finalStockPrice(x):
    start = x[0]  #get the starting price
    change = sum(x[1])
    final = start + change
    return final

stock1 = [10, [1,-.5,2,-1.45]]
stock2 = [2, [.4, -.2,.1,.05,-.23,.03]]
stock3 = [400,[10,-9,9,9,-20,24,-22,100,-24,-23]]
stocks = [stock1, stock2, stock3]
for i in stocks:
    print(finalStockPrice(i))