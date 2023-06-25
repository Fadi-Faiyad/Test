def hello():
    print("hello its me")

def pack(num1, num2, num3):
    packed_list = [num1, num2, num3]
    return packed_list

def eat_lunch(anything_list):
    if not anything_list:
        print("my lunchbox is empty")
    else:
        print(f"first i eat {anything_list[0]}")
        for food in anything_list[1:]:
            print(F"Next i eat {food}")

packed_items = pack("Apple", "Banana", "Orange")
print(packed_items)

food_list = ["Sandwich", "Chips", "Salad"]
eat_lunch(food_list)