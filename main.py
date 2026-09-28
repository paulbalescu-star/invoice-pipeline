import json

with open("invoices.json", encoding="utf-8") as f:
    invoices = json.load(f)

#citeste furnizorul
for invoice in invoices:
    print(f" Pentru furnizorul {invoice.get("supplier")} totalule este {invoice.get("total")} ")