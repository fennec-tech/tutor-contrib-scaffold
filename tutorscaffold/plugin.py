""" This plugin extends tutor with a plugin"""
# import os
# import tempfile
# import requests

import click
from cookiecutter.main import cookiecutter
from tutor import hooks
from .__about__ import __version__

TEMPLATES = {
    "tutor-plugin": {
        "name": "Tutor Plugin",
        "source": "https://github.com/overhangio/cookiecutter-tutor-plugin",
    },
    "tutor-mfe-plugin": {
        "name": "Tutor Plugin",
        "source": "https://github.com/fennec-tech/cookiecutter-tutor-mfe-plugin",
    },

    ## Next on the list
    # "openedx-plugin": {}
    # "openedx-xblock": {}
    # "theme": {}
    # ...
}

DEFAULT_TEMPLATE_ID = "tutor-plugin"

# def template_cache_name(template_name: str) -> str:
#     """ Generates a folder template cache key"""
#     return f"tutor-plugins-scaffold-template-{template_name}"

# @click.group(help="Extra 'dev' commands for managing named volumes")
# def scaffold():
#     pass
@click.command(
    short_help="Create the scaffolding given a specified template",
    help="Creates the scaffolding for a new plugin."
         "You can optionally specify a template using a specified template",
)
@click.argument('template', default=DEFAULT_TEMPLATE_ID)
def scaffold(template):
    """Call 'create' command"""
    # Use a predefined template if the --template option is not specified
    template_info = TEMPLATES.get(
        template,
        {
            "name":"custom",
            "source": template,
        },
    )

    print(f"Using '{template_info['name']}' template located at '{template_info['source']}'.")
    cookiecutter(template_info['source'])

hooks.Filters.CLI_COMMANDS.add_item(scaffold)