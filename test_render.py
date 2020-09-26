from converter import render_to_html


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
    html = render_to_html({"h1": "Title #1", "p": "Hello, World 1!"})
    assert html == "<h1>Title #1</h1><p>Hello, World 1!</p>"
