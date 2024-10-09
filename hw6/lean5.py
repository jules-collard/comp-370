def get_sales(**product_years):
    sales = {}
    for product, years in product_years.items():
        sales["product"] = {year : load("data/{product}_sales_{year}.csv".format(product = product, year = year)) for year in years}
    
    return sales

def get_total_sales(sales, *years):
    totals = {}
    for year in years:
        totals[year] = sum_sales(*[sales[product][year] for product in sales.keys()])

    return totals