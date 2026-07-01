product_price = float(input("Enter Product Price: ₹"))
gst = float(input("Enter GST Percentage (%): "))
gst_amount = (product_price * gst) / 100
final_price = product_price + gst_amount
print("\n------ GST BILL ------")
print("Product Price : ₹", product_price)
print("GST           :", gst, "%")
print("GST Amount    : ₹", gst_amount)
print("----------------------")
print("Final Price   : ₹", final_price)