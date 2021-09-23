import inquirer
import click
import glob
import os
import sys

def choice_envpath(envdir, message="Select Singlarity Environment File"):
    assert envdir is not None

    envfiles = [os.path.basename(path) for path in glob.glob(os.path.join(envdir, "*.sif"))]
    questions = [
        inquirer.List(
            "name",
            message=message,
            choices=envfiles,
        ),
    ]
    envfile = inquirer.prompt(questions)['name']
    envpath = os.path.join(envdir, envfile)
    return envpath

def interactive_command(cmd, environ=os.environ):
    cmd = cmd.split()
    os.spawnvpe(os.P_WAIT, cmd[0], cmd, environ)

def run_singularity_command(envpath, environ=os.environ):
    environ = {"SINGULARITY_SHELL": "/bin/bash", **environ}
    interactive_command(f"singularity shell --nv --bind /doc,/data {envpath}", environ=environ)

@click.command()
@click.option('--envdir', '-e')
def main(**kwargs):
    envpath = choice_envpath(kwargs['envdir'])
    run_singularity_command(envpath)

if __name__ == '__main__':
    main()