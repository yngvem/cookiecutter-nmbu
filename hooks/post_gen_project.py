#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_tree(folderpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, folderpath))


if __name__ == '__main__':
    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if not {{ cookiecutter.sphinx }}:
        remove_tree('docs')

    if not {{ cookiecutter.test }}:
        remove_tree('tests')

    if not {{ cookiecutter.travis }}:
        remove_file('.travis.yml')

