from dataclasses import dataclass

@dataclass(frozen=True)
class MarginInput:
    sales_price: float
    material_cost: float
    production_cost: float

@dataclass(frozen=True)
class MarginOutput:
    total_cost: float
    margin: float
    margin_percent: float

# Calculate the margin
def calculate_margin(data: MarginInput) -> MarginOutput:

    total_cost =  data.material_cost + data.production_cost
    
    margin = data.sales_price - total_cost 

    margin_percent = (
            margin / data.sales_price * 100
            if data.sales_price
            else 0.0
            )

    return MarginOutput(
            total_cost=total_cost,
            margin=margin,
            margin_percent = margin_percent
            )
