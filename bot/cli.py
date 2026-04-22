import argparse
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

from rich.console import Console
from rich.table import Table
from rich import print

console = Console()

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    if not args.symbol:
        args.symbol = input("Enter symbol (e.g., BTCUSDT): ")

    if not args.side:
        args.side = input("Enter side (BUY/SELL): ").upper()

    if not args.type:
        args.type = input("Enter order type (MARKET/LIMIT): ").upper()

    if not args.quantity:
        args.quantity = float(input("Enter quantity: "))

    if args.type == "LIMIT" and not args.price:
        args.price = float(input("Enter price: "))

    if args.type == "STOP_LIMIT" and not args.stop_price:
        args.stop_price = float(input("Enter stop price: "))

    try:
        validate_input(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price
        )

        # Pretty Table Output
        console.print("\n[bold cyan]📌 Order Request Summary[/bold cyan]")

        table = Table()
        table.add_column("Field", style="green")
        table.add_column("Value", style="yellow")

        for k, v in vars(args).items():
            table.add_row(k, str(v))

        console.print(table)

        # Place Order
        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price
        )

        if order:
            console.print("\n[bold green]✅ Order Successful![/bold green]")
            console.print(f"Order ID: {order.get('orderId')}")
            console.print(f"Status: {order.get('status')}")
            console.print(f"Executed Qty: {order.get('executedQty')}")
            console.print(f"Avg Price: {order.get('avgPrice', 'N/A')}")
        else:
            console.print("\n[bold red]❌ Order Failed[/bold red]")

    except Exception as e:
        console.print(f"\n[bold red]⚠️ Error: {str(e)}[/bold red]")

if __name__ == "__main__":
    main()