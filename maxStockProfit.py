#Author chriskbwong
#Assumes that you can only buy one share at a time 
def maxProfit(price, n):

  profit = [0]*n #initialize a new array to save potential profit 
  max_price = price[n-1] #assumes the highest price is at the end of the array

  for i in range(n-2, 0 ,-1): #goes through the list from right to left
    if price[i] > max_price:  #checks if the current value is greater 
      max_price = price[i] #changes the highest price
    profit[i] = max(profit[i+1], max_price - price[i]) 
    #stores the profit of all the values when compared to the max price
        
  min_price=price[0] #starts the min price at the first value
     
  for i in range(1,n): 
    if price[i] < min_price: 
      min_price = price[i]
    profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
         
  result = profit[n-1]
     
  print (result)

#test cases
price = [50, 40, 5, 30, 28, 25, 80]
#buy at 5 sell at 30, buy at 25 sell at 80 total profit of 80 (25+55)
maxProfit(price, len(price))
