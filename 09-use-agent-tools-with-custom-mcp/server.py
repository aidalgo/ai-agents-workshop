# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Inventory")

# Add an inventory check tool
@mcp.tool()
def get_inventory_levels() -> dict:
     """Returns current inventory for all products."""
     return {
         "Moisturizer": 6,
         "Shampoo": 8,
         "Body Spray": 28,
         "Hair Gel": 5, 
         "Lip Balm": 12,
         "Skin Serum": 9,
         "Cleanser": 30,
         "Conditioner": 3,
         "Setting Powder": 17,
         "Dry Shampoo": 45
     }


# Add a weekly sales tool
@mcp.tool()
def get_weekly_sales() -> dict:
     """Returns number of units sold last week."""
     return {
         "Moisturizer": 22,
         "Shampoo": 18,
         "Body Spray": 3,
         "Hair Gel": 2,
         "Lip Balm": 14,
         "Skin Serum": 19,
         "Cleanser": 4,
         "Conditioner": 1,
         "Setting Powder": 13,
         "Dry Shampoo": 17
     }

# Add a product details tool
@mcp.tool()
def get_product_details(product_name: str) -> dict:
    """Returns details for a specific product."""
    product_details = {
        "Moisturizer": {"price": 15.99, "category": "Skincare", "brand": "Glow"},
        "Shampoo": {"price": 12.99, "category": "Haircare", "brand": "Shine"},
        "Body Spray": {"price": 9.99, "category": "Fragrance", "brand": "Fresh"},
        "Hair Gel": {"price": 8.99, "category": "Haircare", "brand": "Style"},
        "Lip Balm": {"price": 3.99, "category": "Skincare", "brand": "Soft"},
        "Skin Serum": {"price": 25.99, "category": "Skincare", "brand": "Radiant"},
        "Cleanser": {"price": 10.99, "category": "Skincare", "brand": "Pure"},
        "Conditioner": {"price": 11.99, "category": "Haircare", "brand": "Smooth"},
        "Setting Powder": {"price": 14.99, "category": "Makeup", "brand": "Flawless"},
        "Dry Shampoo": {"price": 7.99, "category": "Haircare", "brand": "Quick"}
    }
    return product_details.get(product_name, {})



mcp.run()