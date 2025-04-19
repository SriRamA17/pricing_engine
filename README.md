# Dynamic Pricing Engine

## Overview
This script reads product and sales data from CSV files, applies business rules to adjust prices dynamically based on stock and demand, and outputs a new pricing file with updated values.

## Pricing Rules
1. **Low Stock, High Demand:** Increase price by 15%
2. **Dead Stock:** Decrease price by 30%
3. **Overstocked Inventory:** Decrease price by 10%
4. **Minimum Profit Constraint:** Ensure new price is at least 20% above cost

Only the first applicable rule (1–3) is applied, followed by Rule 4.

## Input Files
- `products.csv`
- `sales.csv`

## Output
- `updated_prices.csv` with:
  - `sku`
  - `old_price` (₹)
  - `new_price` (₹)

## How to Run
```bash
python pricing_engine.py
```

## Author
Sriram