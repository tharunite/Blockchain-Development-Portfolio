import hashlib
import random
import time

class LiquidityPool:
    def __init__(self):
        self.USDC = 100000   # token X
        self.ETH = 100       # token Y
        self.fees_percent = 0.003  # 0.3%

    def effective(self, x):
        return x * (1 - self.fees_percent)

    def show_reserve(self):
        return {"USDC": round(self.USDC, 4), "ETH": round(self.ETH, 4)}

    def exchange(self, token_in, amount_in):
        if token_in == "USDC":
            x, y = self.USDC, self.ETH
        elif token_in == "ETH":
            x, y = self.ETH, self.USDC
        else:
            raise ValueError("token_in must be 'USDC' or 'ETH'")

        k = x * y
        new_x = x + amount_in
        new_y = k / new_x
        amount_out = y - new_y
        return amount_out

    def show_exchange_value(self, token_in, sent):
        effective_value = self.effective(sent)
        amount_out = self.exchange(token_in, effective_value)

        if token_in == "USDC":
            pre_price = self.USDC / self.ETH
            post_price = (self.USDC + sent) / (self.ETH - amount_out)
        else:
            pre_price = self.ETH / self.USDC
            post_price = (self.ETH + sent) / (self.USDC - amount_out)

        slippage = (post_price - pre_price) / pre_price
        return round(amount_out, 6), round(slippage * 100, 4)

    def confirm_transaction(self, token_in, sent):
        effective_value = self.effective(sent)
        amount_out = self.exchange(token_in, effective_value)

        if token_in == "USDC":
            self.USDC += sent
            self.ETH -= amount_out
        elif token_in == "ETH":
            self.ETH += sent
            self.USDC -= amount_out

        return {
            "received": round(amount_out, 6),
            "new_reserves": self.show_reserve()
        }

# ---------------- MONTE CARLO SIMULATION ---------------- #

def monte_carlo_simulation(num_trades=100, delay=2):
    pool = LiquidityPool()
    print("\n🚀 Starting AMM Monte Carlo Simulation")
    print("Initial reserves:", pool.show_reserve())

    for i in range(1, num_trades + 1):
        time.sleep(delay)

        # Randomly choose direction
        token_in = random.choice(["USDC", "ETH"])

        # Random trade size (keep realistic bounds)
        if token_in == "USDC":
            amount_in = random.uniform(10, 2000)   # 10–2000 USDC
        else:
            amount_in = random.uniform(0.01, 2)    # 0.01–2 ETH

        amount_out, slippage = pool.show_exchange_value(token_in, amount_in)
        result = pool.confirm_transaction(token_in, amount_in)

        output_token = "ETH" if token_in == "USDC" else "USDC"

        print(f"\n💱 Transaction #{i}")
        print(f"Trader swapped {round(amount_in,4)} {token_in} → {result['received']} {output_token}")
        print(f"Slippage: {slippage}% | Fee: {pool.fees_percent*100:.2f}%")
        print("Updated reserves:", result["new_reserves"])

    print("\n🏁 Simulation completed!")
    print("Final reserves:", pool.show_reserve())

# Run simulation
if __name__ == "__main__":
    monte_carlo_simulation(num_trades=100, delay=2)
