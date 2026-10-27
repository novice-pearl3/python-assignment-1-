from pipeline.validator import validate_record

def test_valid_record():

    record = {
        "branch_id": "BOOK01",
        "date": "2026-10-01",
        "customer_tier": "Gold",
        "items": 3,
        "revenue": 250.00

    }

    assert validate_record(record) == True