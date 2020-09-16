

class Dict:

    @staticmethod
    def create(price: str, usage_fee: str, initial_cost: str, name: str,
             floor_plan: str, area: str, capacity: str, address: str):
        return {
            'Price per month': price,
            'Usage fee': usage_fee,
            'Initial cost': initial_cost,
            'Name of listing': name,
            'Floor plan': floor_plan,
            'Occupied area (size)': area,
            'Capacity': capacity,
            'Address': address,            
        }
