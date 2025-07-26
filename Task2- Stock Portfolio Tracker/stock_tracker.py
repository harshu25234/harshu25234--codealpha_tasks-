# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300,
    "AMZN": 130
}

# Dictionary to store user's stock and quantity
user_portfolio = {}

# Ask user how many different stocks they want to enter
num_stocks = int(input("📈 How many different stocks do you want to enter? "))

# Input loop
for _ in range(num_stocks):
    stock_name = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    quantity = int(input(f"Enter quantity for {stock_name}: "))
    
    if stock_name in stock_prices:
        user_portfolio[stock_name] = quantity
    else:
        print(f"⚠️ Warning: {stock_name} is not in our stock list. Skipping.")

# Calculate total investment
total_value = 0
print("\n🧾 Investment Summary:")
for stock, qty in user_portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to a .txt file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as file:
        file.write("Investment Summary:\n")
        for stock, qty in user_portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("📁 Summary saved to 'investment_summary.txt'")
