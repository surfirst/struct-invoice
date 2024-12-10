from typing import List
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field

class InvoiceItem(BaseModel):
    description: str = Field(..., description="Description of the item")
    quantity: float = Field(..., description="Quantity of the item")
    unit_price: Decimal = Field(..., description="Price per unit")
    total: Decimal = Field(..., description="Total price for this item")
    tax_rate: float = Field(..., description="Tax rate as percentage")

class Invoice(BaseModel):
    invoice_number: str = Field(..., description="Unique invoice identifier")
    date: datetime = Field(..., description="Invoice issue date")    
    total_amount: Decimal = Field(..., description="Total invoice amount")
    vendor_name: str = Field(..., description="Name of the vendor")
    vendor_address: str = Field(..., description="Complete address of the vendor")
    items: List[InvoiceItem] = Field(default_factory=list, description="List of invoice items")    
    tax_amount: Decimal = Field(..., description="Total tax amount")
    
