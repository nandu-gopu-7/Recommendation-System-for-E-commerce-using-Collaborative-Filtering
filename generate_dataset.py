import pandas as pd
import random

# Set random seed for consistent results
random.seed(42)

# Define categories and some example products
categories_products = {
    'Electronics': [
        'iPhone 15', 'Samsung Galaxy S23', 'Redmi Note 12', 'OnePlus 11', 'Sony WH-1000XM4',
        'JBL Bluetooth Speaker', 'Apple Airpods Pro', 'Samsung Smartwatch', 'Dell Inspiron Laptop', 'Mi Powerbank',
        'HP Wireless Mouse', 'Canon DSLR Camera', 'Boat Rockerz Headphones', 'iPad Air', 'Kindle Paperwhite',
        'Samsung 4K TV', 'Sony PlayStation 5', 'GoPro Hero10', 'Amazon Echo Dot', 'Realme Buds Air'
    ],
    'Fashion': [
        'Levi\'s Jeans', 'Nike Air Max', 'Adidas Hoodie', 'Puma Sports Shoes', 'Woodland Boots',
        'H&M Casual Shirt', 'Zara Denim Jacket', 'Forever 21 Skirt', 'RayBan Sunglasses', 'Gucci Belt',
        'UCB Polo T-Shirt', 'HRX Tracksuit', 'Biba Kurti', 'Pepe Jeans Top', 'Tommy Hilfiger Watch',
        'Reebok Running Shoes', 'Allen Solly Formal Shirt', 'Louis Philippe Blazer', 'Roadster Leather Jacket', 'Van Heusen Trousers'
    ],
    'Home Appliances': [
        'LG Washing Machine', 'Samsung Refrigerator', 'Whirlpool Microwave', 'Dyson Vacuum Cleaner', 'Philips Air Fryer',
        'IFB Dishwasher', 'Bajaj Room Heater', 'Orient Ceiling Fan', 'Voltas AC', 'Havells Geyser',
        'Bosch Mixer Grinder', 'Kent Water Purifier', 'Prestige Induction Cooktop', 'Morphy Richards OTG', 'Usha Pedestal Fan',
        'Blue Star Deep Freezer', 'Godrej Air Conditioner', 'Crompton Desert Cooler', 'Eureka Forbes Vacuum', 'Pigeon Rice Cooker'
    ],
    'Beauty Products': [
        'Lakme Lipstick', 'Maybelline Foundation', 'Mamaearth Face Wash', 'L\'Oreal Shampoo', 'Dove Body Lotion',
        'Nivea Deodorant', 'Biotique Face Cream', 'The Body Shop Body Butter', 'Neutrogena Sunscreen', 'Garnier Hair Color',
        'Plum Night Cream', 'Sugar Eyeliner', 'WOW Skin Science Shampoo', 'Nykaa Matte Lipstick', 'Himalaya Face Pack',
        'Pond\'s Moisturizer', 'Tresemme Conditioner', 'Minimalist Serum', 'MCaffeine Coffee Scrub', 'Colorbar Nail Polish'
    ],
    'Grocery': [
        'Aashirvaad Atta', 'Fortune Sunflower Oil', 'Daawat Basmati Rice', 'Nestle Everyday Milk Powder', 'Tata Tea Premium',
        'Kellogg\'s Cornflakes', 'Amul Butter', 'Britannia Bread', 'Parle-G Biscuits', 'MTR Ready to Eat',
        'Saffola Oats', 'Catch Spices', 'Maggi Noodles', 'Tropicana Juice', 'Organic India Tulsi Tea',
        'Haldiram\'s Snacks', 'Sunfeast Pasta', 'Patanjali Honey', 'Mother Dairy Paneer', 'Everest Masala'
    ]
}

# Generate a list of users
user_ids = [f'user_{i}' for i in range(1, 501)]  # 500 users

# Now create user-product interactions
data = []

for user_id in user_ids:
    # Each user buys 3 to 7 products randomly
    number_of_purchases = random.randint(3, 7)
    for _ in range(number_of_purchases):
        category = random.choice(list(categories_products.keys()))
        product = random.choice(categories_products[category])
        product_id = f"P{random.randint(1000, 9999)}"
        
        data.append({
            "user_id": user_id,
            "product_id": product_id,
            "product_name": product,
            "category": category
        })

# Create dataframe
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("amazon_new.csv", index=False)

print("✅ Successfully created 'amazon_new.csv'!")
