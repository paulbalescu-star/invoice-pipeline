import json
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def load_all_invoices(folder):
    invoices = []
    for path in Path(folder).glob("*.json"):
        try:
            with open(path, encoding="utf-8") as f:
                invoices.append(json.load(f))
        except json.JSONDecodeError:
            logger.warning("Invalid File, passed: %s", path)
    logger.info("Loaded %d valid invoices", len(invoices))
    return invoices

def total_by_supplier(invoices):
    totals = {}
    for invoice in invoices:
        #get the supplier and the total of the current invoice
        supplier = invoice["supplier"]
        amount = invoice["total"]
        #check if supplier is already in totals
        if supplier not in totals:
            #add the supplier in the list
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
    if not invoices:
        return None
    max_invoice = invoices[0]
    max_amount = max_invoice["total"]
    for invoice in invoices:
        #get the supplier and the total of the current invoice
        supplier = invoice["supplier"]
        amount = invoice["total"]
        if amount > max_amount:
            max_amount = amount
            max_invoice = invoice
    return max_invoice

def main():

    invoices = load_all_invoices("data")

    print(f" Total amount of each supplier: \n{total_by_supplier(invoices)}\n")

    mismatches = find_mismatches(invoices)
    print(f"Wrong invoices: {mismatches} \n")
    
    max_invoice = find_max_invoice(invoices)

    if(max_invoice != None):
        print(f"The highest invoice: \n {max_invoice}") 
    else:
        print(" No invoices")

if __name__ == "__main__":
    main()