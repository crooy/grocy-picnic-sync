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
@click.argument('query')
def sync_products(query):
   jsonPrint(app.searchProducts(query)); 
   id = click.prompt('Which product do you want to import', type=str)  
   click.echo(f"searching for {id}");
   jsonPrint(app.syncProduct(id))


def jsonPrint(output: str):
    return click.echo(json.dumps(output, indent=2));