#stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that
#will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
#pe ratio = price / earnings per share
#price to book ratio = price / book value

with open (r'C:\\Users\\SESA610197\\Documents\\AIMLLNG\\Python Learning\\Read, Write Practice\\stocks.csv', "r") as f, open (r'C:\\Users\\SESA610197\\Documents\\AIMLLNG\\Python Learning\\Read, Write Practice\\output.csv', "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{stock},{pe},{pb}\n")
    

           
           
