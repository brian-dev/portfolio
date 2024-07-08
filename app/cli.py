import os
from flask import Blueprint
import click

bp = Blueprint('cli', __name__, cli_group=None)


@bp.cli.group()
def translate():
    """Translation and localization commands."""
    pass


@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.po .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel init -i messages.po -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.po')


@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.po .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.po -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.po')


@translate.command()
def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')
