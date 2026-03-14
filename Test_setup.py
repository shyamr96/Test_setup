print('setup')
a=5;
b=10;
print(a+b)

i=0
while i <a:
    print(i)
    i=i+1

i=0
while i <a:
    print(i)
    i=i+2

### always add comments


###test import in new env
import pandas as pd
print('pandas done')

# function to calculate price elasticity
def calculate_price_elasticity(df, price_col, quantity_col):
    # Calculate the percentage change in price and quantity
    df['price_change'] = df[price_col].pct_change()
    df['quantity_change'] = df[quantity_col].pct_change()
    # Calculate price elasticity
    df['price_elasticity'] = df['quantity_change'] / df['price_change']
    return df

# call above function here with some dummy data
data = {
    'price': [10, 12, 14, 16, 18],
    'quantity': [100, 90, 80, 70, 60]
}                                   

df = pd.DataFrame(data)
result = calculate_price_elasticity(df, 'price', 'quantity')
print(result)

print('execute same with class now')
# convert above function to class and then call the function from class
class PriceElasticityCalculator:
    def __init__(self, df):
        self.df = df

    def calculate_price_elasticity(self, price_col, quantity_col):
        # Calculate the percentage change in price and quantity
        self.df['price_change'] = self.df[price_col].pct_change()
        self.df['quantity_change'] = self.df[quantity_col].pct_change()
        # Calculate price elasticity
        self.df['price_elasticity'] = self.df['quantity_change'] / self.df['price_change']
        return self.df
# call above class and function here with some dummy data
data = {
    'price': [10, 12, 14, 16, 18],
    'quantity': [100, 90, 80, 70, 60]
}

df = pd.DataFrame(data)
calculator = PriceElasticityCalculator(df)
result = calculator.calculate_price_elasticity('price', 'quantity')
print(result)
