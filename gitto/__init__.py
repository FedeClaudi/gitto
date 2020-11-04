from rich import print
import os
import click

mocassin = '#FFE4B5'
orange = '#FFA500'



@click.command()
@click.option("-m", "--message", default=None)
@click.option('-f', '--files', multiple=True, default=None)
def commit(message=None, files=None):
    message = message or 'bump'

    # Add files
    print(f'[{mocassin}]Adding files to commit ([{orange}]{message}[/{orange}])')
    try:
        files[0]
        os.system(f'git add {" ".join(files)}')
    except IndexError:
        os.system(f'git add .')

    print(f'\n\n[{mocassin}]Executing commit ([{orange}]{message}[/{orange}])')
    os.system(f'git commit -m {message}')
    os.system(f'git push')