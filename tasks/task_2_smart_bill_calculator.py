"""Task 2 — Smart Bill Calculator
Ek item ka price aur quantity maango. Total nikaalo. Agar total 1000 se zyada hai toh 10% discount lagao, warna koi discount nahi. Final amount 2 decimals ke saath print karo.

Concepts: arithmetic, if/else, f-string formatting :.2f
Hint: discount = total * 0.10 sirf tab jab total > 1000."""




"""item_price = float(input("Enter item price: "))
item_quantity = int(input("Enter the quantity of items: "))
total = item_price * item_quantity

if total > 1000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\n")
print("=====Bill=====")
print(f"Total Bill: {total: .2f}")
print(f"Discount: {discount: .2f}")
print(f"Final Amount: {final_amount: .2f}")"""







price = float(input("Enter price: "))
quantity = int(input("Enter qunatity: "))
total = price * quantity

if total > 1000:
    discount = total * 0.10
else: 
    discount = 0

final_amount = total - discount    

print("\n")
print("==========Bill==========")
print(f"Total: {total: .2f}")
print(f"Discount: {discount: .2f}")
print(f"Final Amount: {final_amount: .2f}")
print("=" * 25)
