from collections import defaultdict
from datetime import datetime
import os


def parse_transactions(lines):
    header = lines[0].strip().split("|")
    transactions = []

    for line in lines[1:]:
        values = line.strip().split("|")
        if len(values) != len(header):
            continue

        record = dict(zip(header, values))
        try:
            record["Quantity"] = int(record["Quantity"])
            record["UnitPrice"] = float(record["UnitPrice"])
            record["Revenue"] = record["Quantity"] * record["UnitPrice"]
            transactions.append(record)
        except:
            continue

    return transactions


def validate_transactions(transactions):
    valid = []
    invalid = []

    for t in transactions:
        if t["Quantity"] > 0 and t["UnitPrice"] > 0:
            valid.append(t)
        else:
            invalid.append(t)

    return valid, invalid


def total_revenue(transactions):
    return sum(t["Revenue"] for t in transactions)


def region_wise_sales(transactions):
    regions = defaultdict(lambda: {"sales": 0, "count": 0})
    for t in transactions:
        regions[t["Region"]]["sales"] += t["Revenue"]
        regions[t["Region"]]["count"] += 1
    return regions


def top_products(transactions, top_n=5):
    products = defaultdict(lambda: {"qty": 0, "rev": 0})
    for t in transactions:
        products[t["ProductName"]]["qty"] += t["Quantity"]
        products[t["ProductName"]]["rev"] += t["Revenue"]

    return sorted(products.items(), key=lambda x: x[1]["rev"], reverse=True)[:top_n]


def generate_sales_report(transactions, enriched, output_file="output/sales_report.txt"):
    os.makedirs("output", exist_ok=True)

    total_rev = total_revenue(transactions)
    regions = region_wise_sales(transactions)
    products = top_products(transactions)

    report = []
    report.append("SALES ANALYTICS REPORT")
    report.append("=====================")
    report.append(f"Generated: {datetime.now()}")
    report.append(f"Total Transactions: {len(transactions)}")
    report.append(f"Total Revenue: {total_rev}")
    report.append("")

    report.append("REGION WISE SALES")
    for r, v in regions.items():
        report.append(f"{r}: {v['sales']} ({v['count']} transactions)")

    report.append("")
    report.append("TOP PRODUCTS")
    for i, (p, d) in enumerate(products, 1):
        report.append(f"{i}. {p} | Qty: {d['qty']} | Revenue: {d['rev']}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
