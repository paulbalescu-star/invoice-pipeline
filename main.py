import json

def load_invoices(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def total_by_supplier(invoices):
    totals = {}
    for invoice in invoices:
        #get the supplier and the total of the current invoice
        supplier = invoice["supplier"]
        amount = invoice["total"]
        #check if supplier is already in totals
        if supplier not in totals:
            #add the current value to the total
            totals[supplier] = 0
        totals[supplier] += amount
    return totals
    

def find_mismatches(invoices):
    wrong_invoices = []
    for invoice in invoices:
        #get the net,vat and the total of the current invoice
        net = invoice["net"]
        vat = invoice["vat"]
        total = invoice["total"]
        #check if the total is correct
        if abs(net + vat - total) > 0.01:
            wrong_invoices.append(invoice["number"])
    return wrong_invoices

def find_max_invoice(invoices):
    max_invoice = invoices[0]
    max_amount = max_invoice["total"]
    for invoice in invoices:
        #get the supplier and the total of the current invoice
        supplier = invoice["supplier"]
        amount = invoice["total"]
        if amount > max_amount:
            max_amount = amount
            max_invoice = invoice
    return max_invoice;

def main():
    #load invoices
    invoices = load_invoices("invoices.json")
    #calculate the total by supplier
    print(f" Total amount of each supplier: \n{total_by_supplier(invoices)}\n")
    #find mismatched invoices
    print(f"Wrong invoices: {find_mismatches(invoices)} \n")
    #find highest invoice
    print(f"The highest invoice: \n {find_max_invoice(invoices)}")


    

if __name__ == "__main__":
    main()