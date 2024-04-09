import argparse
import typing
from importlib.resources import as_file, files
from string import Template

import pyperclip

import const


def copy_to_clipboard(text: str):
    pyperclip.copy(text)
    print(f'=== OUTPUT BELOW COPIED TO CLIPBOARD ===')
    print(text)


def get_template(template_path: str) -> Template:
    source = files(const.TEMPLATE_DIR).joinpath(template_path)

    with as_file(source) as template_text:
        t_text = template_text.read_text()
        return Template(template=t_text)


def request_inputs(identifiers: typing.List[str]):
    return {field: input(f'Enter {field}: ').strip() for field in identifiers}


def process_template(template_path: str):
    template = get_template(template_path=template_path)
    context = request_inputs(identifiers=template.get_identifiers())
    output = template.substitute(**context)
    copy_to_clipboard(output)


parser = argparse.ArgumentParser()

parser.add_argument("--template-path", dest="template_path", help="Enter template path")
args = parser.parse_args()
process_template(template_path=args.template_path)
