# Norwegian is only kept for compliance with task

# Reads a file of cold calling seller stats and converts to dictionary
def innlesing(filnavn):
    
    sales_stats = {}
    
    f = open(filnavn, "r")

    for line in f:
        stat = line.split()
        sales_stats[stat[0]] = int(stat[1])
    
    f.close()

    return sales_stats

# Prints the seller with the highest sales given a dict with seller statistics
def maanedensSalgsperson(seller_stats):
    
    sales = 0
    
    for k, v in seller_stats.items():
        if v > sales:
            seller = k
            sales = v

    print("Maanedens ansatte er %s med %d salg!" % (seller, sales))

# Returns the total sales given a dict with seller statistics
def totaltAntallSalg(seller_stats):
    
    sales = 0

    for val in seller_stats.values():
        sales += int(val)

    return sales

# Returns the average sales per seller given a dict of seller statistics
def gjennomsnittSalg(seller_stats):
    
    sales= totaltAntallSalg(seller_stats)
    
    sellers = len(seller_stats.keys())
    
    avg = float(sales/sellers)
    
    return avg
    
# Main function
def hovedprogram():
    
    fil = "salgstall.txt"
    
    stats = innlesing(fil)    

    maanedensSalgsperson(stats)
    
    print("Aktive selgere denne maaneden: %d" % len(stats.keys()))
    print("Totalt antall salg: %d" % totaltAntallSalg(stats))
    print("Gjennomsnittlig antall salg per salgsperson: %.2f" % gjennomsnittSalg(stats))

# Runs the main
hovedprogram()
