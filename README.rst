Scaffold plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================
This WIP Tutor plugin adds a ``tutor scaffold`` which produces the scaffoldings for various Tutor and Open edX projects.

Installation
------------
.. code: bash
   pip install git+https://github.com/fennec-tech/tutor-contrib-scaffold

Usage
-----
Enable the plugin in tutor
.. code: bash
   tutor plugins enable scaffold

Then, run the command
.. code: bash
   tutor scaffold <template-name>

The project will be generated in the working directory.
Supported templates
###################

- ``tutor-plugin``: official `Tutor plugin cookiecutter <https://github.com/overhangio/cookiecutter-tutor-plugin>`__
- ``tutor-mfe-plugin``: official `Tutor plugin cookiecutter <https://github.com/overhangio/cookiecutter-tutor-plugin>`__
- any cookiecutter template, following ``cookiecutter``'s syntax. It can be a local directory, a zip file, a remote repository, etc.

Troubleshooting
---------------
This Tutor plugin is maintained by `Abderraouf Mehdi Bouhali <https://github.com/ARMBouhali>`__ from `Fennec Technologies <https://fennectech.com>`__ (`@fennec-tech <https://github.com/ARMBouhali>`__). Community support is available from the official `Open edX forum <https://discuss.openedx.org>`_.

Contributing
------------
This project is a work in progress, as it still has few templates which don't cover the needs of Open edX developers and site operators.
Any contributions, suggestions, feature requests or bug reports are welcome on GitHub `issues <https://github.com/fennec-tech/cookiecutter-tutor-mfe-plugin/issues>`__ and `pull requests <https://github.com/fennec-tech/cookiecutter-tutor-mfe-plugin/pulls>`__, as well as on the official Open edX `forum <https://discuss.openedx.org>`__ and `Slack group <https://openedx-slack-invite.herokuapp.com>`__.

Roadmap
#######
- Full support of ``cookiecutter``'s arguments and options.
- More project templates to include (theme, openedx plugin, xblock, etc.)
- Better user-friendly configuration prompt.

License
-------
This software islicensed under the terms of the `AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.en.html>`__. 