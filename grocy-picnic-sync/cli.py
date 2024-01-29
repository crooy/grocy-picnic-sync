"""
Sample App Command-Line Interface
"""
import click
import json
from .app import GrocyPicnicSync

app = GrocyPicnicSync();

@click.group()
def cli():
    x=1

@cli.command()
@click.argument('product')
def sync_products(product):
   jsonPrint(app.syncProducts(product));   

def jsonPrint(output: str):
    return click.echo(json.dumps(output, indent=2));