import click


@click.group(short_help="iauthenfunctions CLI.")
def iauthenfunctions():
    """iauthenfunctions CLI.
    """
    pass


@iauthenfunctions.command()
@click.argument("name", default="iauthenfunctions")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [iauthenfunctions]
