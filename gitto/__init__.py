from rich import print
import os
import click

mocassin = '#FFE4B5'
orange = '#FFA500'
green = '#4ca975'


@click.command()
@click.option("-m", "--message", default=None)
@click.option('-f', '--files', multiple=True, default=None)
@click.option("-p", "--push", is_flag=True, default=False)
def commit(message=None, files=None, push=False):
    message = message or 'bump'
    print(message)

    # Add files
    print(f'[{mocassin}]Adding files to commit ([{orange}]{message}[/{orange}])')
    try:
        files[0]
        os.system(f'git add {" ".join(files)}')
    except IndexError:
        os.system(f'git add .')

    print(f'\n[{mocassin}]Executing commit ([{orange}]{message}[/{orange}])')
    os.system(f'git commit -m "{message}"')

    if push:
        print(f'\n[{mocassin}]Pushing commit ([{orange}]{message}[/{orange}])')
        os.system(f'git push')

    print(f'\n[{green}]Commit [/{green}][{orange}]{message}[/{orange}][{green}] has been [{orange}]{"commited" if not push else "pushed"}')