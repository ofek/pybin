import os
import platform
import subprocess
from site import USER_BASE, USER_SITE

ON_WINDOWS = False
if os.name == 'nt' or platform.system() == 'Windows':  # no cov
    ON_WINDOWS = True


def get_user_base(pypath=None):
    return subprocess.check_output(
        [pypath, '-m', 'site', '--user-base'],
        shell=ON_WINDOWS
    ).decode().strip() if pypath else USER_BASE


def get_user_site(pypath=None):
    return subprocess.check_output(
        [pypath, '-m', 'site', '--user-site'],
        shell=ON_WINDOWS
    ).decode().strip() if pypath else USER_SITE


if ON_WINDOWS:
    def locate(pypath=None):
        return os.path.join(
            os.path.dirname(get_user_site(pypath)),
            'Scripts'
        )


    def put_in_path(pypath=None):
        user_bin_path = locate(pypath)

        # PowerShell will always be available on Windows 7 or later.
        try:
            output = subprocess.check_output(
                ['powershell',
                 '-Command',
                 "& {[Environment]::GetEnvironmentVariable('PATH', 'User')}"],
                shell=True
            ).decode().strip()

            # We do this because the output may contain new lines.
            old_path = ''.join(output.splitlines())
            new_path = '{}{}{}'.format(user_bin_path, os.path.sep, old_path)

            subprocess.check_call(
                ['powershell',
                 '-Command',
                 "& {{[Environment]::SetEnvironmentVariable('PATH', '{}', 'User')}}".format(new_path)],
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError:
            try:
                # https://superuser.com/a/601034/766960
                subprocess.check_call((
                    'for /f "skip=2 tokens=3*" %a in (\'reg query HKCU\Environment '
                    '/v PATH\') do @if [%b]==[] ( @setx PATH "{path};%~a" ) else '
                    '( @setx PATH "{path};%~a %~b" )'.format(path=user_bin_path)
                ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError:
                return False

        return True

else:
    def locate(pypath=None):
        return os.path.join(get_user_base(pypath), 'bin')


    def put_in_path(pypath=None):
        # This function is probably insufficient even though it works in
        # most situations. Please improve this to succeed more broadly!
        user_bin_path = locate(pypath)
        path_line = 'export PATH="{}{}$PATH"\n'.format(user_bin_path, os.path.sep)

        user_profile = os.path.expanduser('~/.profile')
        if os.path.exists(user_profile):
            with open(user_profile, 'r') as f:
                lines = f.readlines()
        else:
            lines = []

        # PATH is likely already defined here but we'll
        # simply redefine it to make our lives easy.
        lines.append(path_line)
        with open(user_profile, 'w') as f:
            f.writelines(lines)


def in_path(pypath=None):
    return locate(pypath) in os.environ['PATH']
