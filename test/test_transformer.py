from pipeline.schema import TransactionRecord
from pipeline.transformer import calculate_net_revenue

def test_net_revenue():

    record = TransactionRecord(
        "BOOK01",
        "2026-10-01",
        "Gold",
        3,
        250.00
    )

    assert calculate_net_revenue(record) == 225.0