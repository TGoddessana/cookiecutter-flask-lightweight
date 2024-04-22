import os
import click


@click.group()
def translate():
    """Translation and localization commands."""
    pass


@translate.command()
def update():
    """Update all translations."""
    click.echo("Updating translations...")

    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        return click.echo("extract command failed")
    if os.system("pybabel update -i messages.pot -d translations"):
        return click.echo("update command failed")

    os.remove("messages.pot")
    click.echo("Updated translations.")


@translate.command()
def compile():
    """Compile all translations."""
    click.echo("Compiling translations...")

    if os.system("pybabel compile -d translations"):
        raise click.echo("compile command failed")

    click.echo("Compiled translations.")


@translate.command()
@click.argument("language")
def init(language):
    """Initialize a new language."""
    click.echo("Initializing new language...")

    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        return click.echo("extract command failed")
    if os.system(f"pybabel init -i messages.pot -d translations -l {language}"):
        return click.echo("init command failed")

    os.remove("messages.pot")
    click.echo(f"Initialized new language: {language}")
