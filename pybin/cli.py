import click

from pybin import in_path, locate, put_in_path


CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
}


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.option('-p', '--pypath', help='An absolute path to a Python executable.')
@click.version_option()
@click.pass_context
def pybin(ctx, pypath):
    """Shows the location of the bin directory and whether or not it is
    in the user PATH.
    """
    if ctx.invoked_subcommand is None:
        location = locate(pypath)
        exists = in_path(pypath)
        click.echo('The user bin directory `{}` is {} in PATH{}'.format(
            location,
            'already' if exists else 'not',
            '!' if exists else '.'
        ))


@pybin.command(context_settings=CONTEXT_SETTINGS,
               short_help='Updates the user PATH')
@click.option('-p', '--pypath', help='An absolute path to a Python executable.')
@click.option('-f', '--force', is_flag=True,
              help='Update PATH even if it appears to be correct.')
def put(pypath, force):
    """Updates the user PATH. The shell must be restarted for the update to
    take effect.
    """
    if not force and in_path(pypath):
        click.echo((
            'The user bin directory `{}` is already in PATH! '
            'Exiting...'.format(locate(pypath))
        ))
        return

    click.echo('Success!' if put_in_path(pypath) else 'Unexpected failure')
