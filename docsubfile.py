from unittest import TestCase

from caseutil import to_kebab
from docsub import click
from doctestcase import to_markdown
from importloc import Location, get_subclasses, random_name


@click.group()
def x() -> None:
    pass


@x.command()
@click.argument('case')
@click.option('-d', '--depth', type=int, default=3)
def case(case: str, depth: int) -> None:
    text = to_markdown(Location(case).load(modname=random_name), title_depth=depth)
    click.echo(text, nl=False)


@x.command()
@click.argument('file')
def caselist(file: str) -> None:
    module = Location(file).load(modname=random_name)
    cases = get_subclasses(module, TestCase)
    cases.sort(key=lambda c: c.__firstlineno__)  # type: ignore
    for case in cases:
        title = to_markdown(case, title_depth=0).split('\n', 1)[0].strip()
        item = f'* [{title}](#{to_kebab(title)})'
        click.echo(item)
