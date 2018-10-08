# Norwegian is only kept for compliance with task

# Function for reading a file of cold calling seller stats
def innlesing(filnavn)
    
    sales_stats = {}
    
    f = open(filnavn, "r")

    for line in f:
        stat = line.split()
        sales_stat{stat[0]} = int(stat[1])
    
    f.close()

    return sales_stats


