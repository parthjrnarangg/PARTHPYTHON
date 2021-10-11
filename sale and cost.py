sale=int(input("inter your sale"))
cost=int(input("inter your cost"))


if cost - sale > 0:
     profit = cost - sale
     print("Profit is",profit)
if sale-cost > 0:
    loss = sale -cost
    print("loss is",loss) 
