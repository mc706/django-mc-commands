import os

from mc_commands._docs import docs as command_docs


def generate_docs(directory):
    if not os.path.exists(os.path.join(directory, 'docs')):
        os.makedirs(os.path.join(directory, 'docs'))
    with (open(os.path.join(directory, 'docs', 'mc_commands.md'), 'w')) as f:
        f.write(command_docs)
