import argparse
import json
import os
import re
import html

BASIC_DIR = os.path.dirname(__file__)

RE_TAG_NAME = re.compile(r"^(\w+)\.?")
RE_TAG_CLASS = re.compile(r"\.(\w+[-_\w]*)")
RE_TAG_ID = re.compile(r"#(\w+[-_\w+]*)")


def render_to_html(source):
    if isinstance(source, list):
        result_html = "".join([render_node(node, wrap_list=True) for node in source])
        return f"<ul>{result_html}</ul>"
    if isinstance(source, dict):
        return render_node(source)
    raise TypeError("Incorrect format. Source data must be a list or dict ")


def parse_tag(tag_string):
    tag_name = RE_TAG_NAME.findall(tag_string)[0]
    tag_classes = " ".join(RE_TAG_CLASS.findall(tag_string))
    tag_id = "".join(RE_TAG_ID.findall(tag_string))
    open_tag = tag_name
    if tag_classes:
        open_tag = f'{open_tag} class="{tag_classes}"'
    if tag_id:
        open_tag = f'{open_tag} id="{tag_id}"'
    return open_tag, tag_name


def render_element(element):
    if isinstance(element, list):
        value = "".join([render_node(subnode, wrap_list=True) for subnode in element])
        result_value = f"<ul>{value}</ul>"
    else:
        result_value = html.escape(element)
    return result_value


def render_node(node, wrap_list=False):
    if isinstance(node, dict):
        res = ""
        for key, value in node.items():
            open_tag, close_tag = parse_tag(key)
            result_value = render_element(value)
            res += f"<{open_tag}>{result_value}</{close_tag}>"
        if wrap_list:
            res = f"<li>{res}</li>"
        return res
    raise TypeError("Node must be a dict")


def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--source-file",
        help="source file format json",
        default=os.path.join(BASIC_DIR, "source.json"),
    )
    parser.add_argument(
        "-o",
        "--output-file",
        help="result file format html",
        default=os.path.join(BASIC_DIR, "index.html"),
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parsing_arguments()
    if not os.path.exists(args.source_file):
        raise FileExistsError(f"Source file {args.source_file} not exists")
    with open(args.source_file) as source_file:
        data = source_file.read()
    deserialize_data = json.loads(data)
    result_html = render_to_html(deserialize_data)
    with open(args.output_file, "w") as html_file:
        html_file.write(result_html)
