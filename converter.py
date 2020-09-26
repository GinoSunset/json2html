import argparse
import json
import os

BASIC_DIR = os.path.dirname(__file__)


def render_to_html(source):
    if isinstance(source, list):
        html = "".join([render_node(node, wrap_list=True) for node in source])
        return f"<ul>{html}</ul>"
    if isinstance(source, dict):
        return render_node(source)
    raise TypeError("Incorrect format. Source data must be a list or dict ")


def render_node(node, wrap_list=False):
    if isinstance(node, dict):
        res = ""
        for key, value in node.items():
            if isinstance(value, list):
                value = "".join(
                    [render_node(subnode, wrap_list=True) for subnode in value]
                )
                value = f"<ul>{value}</ul>"
            res += f"<{key}>{value}</{key}>"
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
    html = render_to_html(deserialize_data)
    with open(args.output_file, "w") as html_file:
        html_file.write(html)
