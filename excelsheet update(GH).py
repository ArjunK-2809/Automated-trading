import openpyxl
# Function to update Excel sheet with fetched data and calculated metrics
def update_excel_sheet(prices_dcx, prices_wazirx, prices_binance, max_dict, min_dict, percentage_dict,profit_loss_dict):
    try:
        #opening the excel sheet if already exists
        wb=openpyxl.load_workbook('crypto_data.xlsx')
    # creating one if doesnot exist
    except FileNotFoundError:
        wb=openpyxl.Workbook()
    # Getting the active sheet of the workbook
    sheet=wb.active

    # If the sheet doesnot have coloumn headers we will add them
    if not sheet['A1'].value=="Cryptocurrency Symbol":
        sheet.append(["Cryptocurrency Symbol","WazirX Price","CoinDCX Price","Binance Price","Max Price","Max Source","Min Price","Min Source","Percentage Difference","Profit/Loss(if you invest 1L INR)"])
    if sheet.dimensions:
        for key in prices_dcx.keys():
            #appending our processed data into the excel sheet
            sheet.append([key.upper(), 
                          prices_wazirx[key],prices_dcx[key],prices_binance[key],max_dict[key][0],max_dict[key][1],min_dict[key][0],min_dict[key][1],percentage_dict[key][0],profit_loss_dict[key][0]])
    # saving the sheet with the processed data
    wb.save('crypto_data.xlsx')

#calling the excel function
update_excel_sheet(price_wazirx, price_dcx, prices_binance, max_dict, min_dict, percentage_dict,profit_loss_dict)
