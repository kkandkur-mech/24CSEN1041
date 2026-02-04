def format_text_for_display(items):
    print(f"{'Item':<20} {'Quantity':<10} {'Price':<10}")
    print("-" * 40)
    
    for item, quantity, price in items:
        print(f"{item:<20} {quantity:<10} {price:<10.2f}")

def calculate_total(items):
    total = sum(quantity * price for _, quantity, price in items)
    return total

# Sample item list
item_list = [
    ("Apple", 10, 0.5),
    ("Banana", 5, 0.3),
    ("Cherry", 15, 0.2)
]

# Display formatted items
format_text_for_display(item_list)

# Calculate total
total_cost = calculate_total(item_list)
print("Total Cost:", total_cost)
#output
Item                 Quantity   Price     
----------------------------------------
Apple                10         0.50      
Banana               5          0.30      
Cherry               15         0.20      
Total Cost: 9.5
