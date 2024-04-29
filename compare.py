max_price_dict = {}
min_price_dict = {}

for key in price_dcx.keys():
    # Get the maximum value and its source
    max_val, max_source = max([(price_dcx[key], 'price_dcx'), (price_wazirx[key], 'price_wazirx'), (prices_binance[key], 'price_binance')])
    max_price_dict[key] = (max_val, max_source)
    
    # Get the minimum value and its source
    min_val, min_source = min([(price_dcx[key], 'price_dcx'), (price_wazirx[key], 'price_wazirx'), (prices_binance[key], 'price_binance')])
    min_price_dict[key] = (min_val, min_source)

print("Maximum values dictionary:", max_price_dict)
print("Minimum values dictionary:", min_price_dict)

# Initialize dictionary to store percentage difference
percentage_dict = {}

# Iterate over keys in the dictionaries again to calculate percentage difference
for key in price_dcx.keys():
    max_val, _ = max_price_dict[key]
    min_val, _ = min_price_dict[key]
    percentage = ((max_val - min_val) / min_val) * 100

    # Add the percentage difference to the new dictionary
    percentage_dict[key] = [percentage,min_price_dict[key][1],max_price_dict[key][1]]

print("Percentage difference dictionary:", percentage_dict)