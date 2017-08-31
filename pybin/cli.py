import click


CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def pybin():
    pass
