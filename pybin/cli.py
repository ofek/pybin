import click

from pybin import in_path, locate, put_in_path


CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
}


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.option('-p', '--pypath')
@click.version_option()
@click.pass_context
def pybin(ctx, pypath):
    if ctx.invoked_subcommand is None:
        location = locate(pypath)
        exists = in_path(pypath)
        click.echo('The user bin directory `{}` is {} in PATH{}'.format(
            location,
            'already' if exists else 'not',
            '!' if exists else '.'
        ))


@pybin.command(context_settings=CONTEXT_SETTINGS)
@click.option('-p', '--pypath')
def put(pypath):
    if in_path(pypath):
        click.echo('The user bin directory `{}` is already in PATH!'.format(locate(pypath)))

    click.echo('Success!' if put_in_path(pypath) else 'Unexpected failure')
