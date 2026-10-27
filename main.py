# milestone 1 
# data ingestion & defensive validation
# other milstone is combined here  

from pipeline.validator import validate_record
from pipeline.schema import TransactionRecord
from pipeline.transformer import calculate_net_revenue
from pipeline.reporter import display_report

raw_data = [
    {
        "branch_id": "BOOK01",
        "date": "2026-10-01",
        "customer_tier": "Gold",
        "items": 3,
        "revenue": 250.00
    },
    {
        "branch_id": "BOOK02",
        "date": "2026-10-02",
        "customer_tier": "Silver",
        "items": 5,
        "revenue": 190.00
    },
    {
        "branch_id": "",
        "date": "2026-10-05",
        "customer_tier": "Bronze",
        "items": 2,
        "revenue": 75.00
    },
    {"branch_id": "BOOK03",
        "date": "2026-10-05",
        "customer_tier": "Bronze",
        "items": 2,
        "revenue": -60.00
    }
]

for record in raw_data:  
    print (validate_record(record))

book = TransactionRecord(
    "BOOK01",
    "2026-10-01",
    "Gold",
    3, 
    250.00
)

print (book.branch_id)

valid_records = []

for record in raw_data:
    if validate_record(record):
        valid_records.append(
            TransactionRecord(
                record["branch_id"],
                record["date"],
                record["customer_tier"],
                record["items"],
                record["revenue"]
            )
        )

print(len(valid_records))

for record in valid_records:
    print(calculate_net_revenue(record))

active_records = list(
    filter(
        lambda record: record.revenue > 0,
        valid_records
    )
)    

print(len(active_records))

total_sales = sum(
    record.revenue for record in valid_records
)

print(total_sales)

branch_totals = {}

for record in valid_records:
    if record.branch_id not in branch_totals:
        branch_totals[record.branch_id] = 0

    branch_totals[record.branch_id] += record.revenue

top_branch = max(
    branch_totals,
    key=branch_totals.get
)

print(top_branch)

customer_tiers = {}

for record in valid_records:

    if record.customer_tier not in customer_tiers:
        customer_tiers[record.customer_tier] = 0

    customer_tiers[record.customer_tier] += 1

print(customer_tiers)

retention_rate = (
    len(valid_records) / len(raw_data)
) * 100

print(retention_rate)

display_report(
    total_sales,
    retention_rate,
    top_branch,
    customer_tiers
)