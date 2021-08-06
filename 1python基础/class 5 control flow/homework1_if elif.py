# price_input=input("请输入价格：")
# price=int(price_input)
# if price <=0:
#     print("请输入大于0 的价格")
# elif price>0 and price<50:
#     total_price=price
#     print(f"您输入的价格没有任何折扣，您的总价格为{total_price}")
# elif price >=50 and price <=100:
#     total_price=price-(price*0.1)
#     print(f"您输入的价格享受10%的折扣，您的最终价格为{total_price}")
# elif price>100:
#     total_price=price-(price*0.2)
#     print(f"您输入的价格享受 20%的折扣,您的最终价格为{total_price}")
price_input=input("请输入价格")
price=int(price_input)
if price<=0:
    print("请输入大于0的价格")
elif price >0 and price<50:
    total_price=price
    print("当前价格没有折扣，您的最终价格为{}".format(total_price))
elif price>=50 and price <=100:
    total_price=price-(price*0.1)
    print("当前价格享受的折扣为10%，您的最终价格为{}".format(total_price))
elif price>100:
    total_price=price-(price*0.2)
    print("当前价格享受的折扣为20%，您的最终价格为{}".format(total_price))