"""
Sample App Command-Line Interface
"""
from .app import GrocyPicnicSync
import click

app = GrocyPicnicSync();

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")

@cli.command()
@click.argument('product')
def sync_products(product):
   click.echo(f"{app.syncProducts(product)}")   

