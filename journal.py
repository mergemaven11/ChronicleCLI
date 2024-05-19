import typer
import cli.handlers as handler
import cli.utils as util  # pytest works but python journal.py wont


app = typer.Typer()

# def main():
#     print("Hello World")

# Add imported commands to the main Typer application instance
@app.command()
def add():
    title = typer.prompt("Please enter a title")
    entry = typer.prompt("Please enter your journal entry")
    # Send data to add handler
    handler.add_entry_to_file({"Title": title, "Entry": entry})
    
    
@app.command()
def view(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def export(name: str):
    typer.echo(f"Hello {name}")

@app.command()
def search(keyword: str):        
    handler.search_entries(keyword)


    
@app.command()
def delete(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def edit(name: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
   # Check if first entry, if so create the dir and file.
   util.check_entries_dir()
   app()