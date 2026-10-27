# milestone 2 

class TransactionRecord: 
    def __init__(self, branch_id, date, customer_tier, items, revenue):
        self.branch_id = branch_id
        self.date = date
        self.customer_tier = customer_tier
        self.items = items 
        self.revenue = revenue 


class RetailAnalytics:
    def __init__(self, records): 
        self.records = records 
        