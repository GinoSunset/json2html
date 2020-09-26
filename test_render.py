from os import openpty
from converter import render_to_html, parse_tag
import pytest


def test_render_with_simple_date_from_example():
    assert (
        render_to_html(
            [
                {
                    "h1": "Title #1",
                    "content": [
                        {"p": "Hello, World 1!", "span": "Woow"},
                    ],
                },
                {"div": "Title #2", "span": "Hello, World 2!"},
            ]
        )
        == "<ul><li><h1>Title #1</h1><content><ul><li><p>Hello, World 1!</p><span>Woow</span></li></ul></content></li><li><div>Title #2</div><span>Hello, World 2!</span></li></ul>"
    )


def test_render_json_without_list():
    html = render_to_html(
        {"h1": "Title #1", "p.active-1.sma_ll#p1": "Hello, World 1!<a>a</a>"}
    )
    assert (
        html
        == '<h1>Title #1</h1><p class="active-1 sma_ll" id="p1">Hello, World 1!&lt;a&gt;a&lt;/a&gt;</p>'
    )


@pytest.mark.parametrize(
    "tag_source_name,expected",
    [
        ("a", "a"),
        ("a.active", 'a class="active"'),
        ("a.active.active-1", 'a class="active active-1"'),
        ("a.active.active-1.active_1", 'a class="active active-1 active_1"'),
        ("a#1", 'a id="1"'),
        ("a#a-1", 'a id="a-1"'),
        ("a#a-1.active", 'a class="active" id="a-1"'),
        ("a#a-1.active!123", 'a class="active" id="a-1"'),
        ("a#a-1..active!123", 'a class="active" id="a-1"'),
        ("a##a-1.active!123", 'a class="active" id="a-1"'),
    ],
)
def test_parse_tag(tag_source_name, expected):
    open_tag, _ = parse_tag(tag_source_name)
    assert open_tag == expected
