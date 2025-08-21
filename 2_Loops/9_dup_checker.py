items=["apple","banana","orange","apple","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate item : ",item)
    else:
        unique_item.add(item)
        