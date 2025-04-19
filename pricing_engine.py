import pandas as pd

# Load input CSV files
products_df = pd.read_csv('products.csv')
sales_df = pd.read_csv('sales.csv')

# Merge the two DataFrames on 'sku'
merged_df = pd.merge(products_df, sales_df, on='sku', how='left')

# Fill missing sales with 0
merged_df['quantity_sold'] = merged_df['quantity_sold'].fillna(0)

# Function to calculate new price
def calculate_new_price(row):
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']

    new_price = current_price

    # Rule 1 – Low Stock, High Demand
    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15

    # Rule 2 – Dead Stock
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.7

    # Rule 3 – Overstocked Inventory
    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.9

    # Rule 4 – Minimum Profit Constraint
    min_allowed_price = cost_price * 1.2
    if new_price < min_allowed_price:
        new_price = min_allowed_price

    # Round to 2 decimal places
    new_price = round(new_price, 2)

    return new_price

# Apply the pricing rules
merged_df['new_price'] = merged_df.apply(calculate_new_price, axis=1)

# Prepare output DataFrame with units (₹)
output_df = merged_df[['sku', 'current_price', 'new_price']].copy()
output_df.rename(columns={'current_price': 'old_price'}, inplace=True)
    
output_df['old_price'] = output_df['old_price'].apply(lambda x: f"₹{x:.2f}")
output_df['new_price'] = output_df['new_price'].apply(lambda x: f"₹{x:.2f}")

# Save to CSV
output_df.to_csv('updated_prices.csv', index=False, encoding='utf-8-sig')
print("✅ Pricing updated and saved to 'updated_prices.csv'")