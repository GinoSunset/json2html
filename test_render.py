from converter import render_to_html


def test_render_with_simple_date_from_example():
    assert (
        render_to_html(
            [
                {"h1": "Title #1", "p": "Hello, World 1!"},
                {"div": "Title #2", "span": "Hello, World 2!"},
            ]
        )
        == "<h1>Title #1</h1><p>Hello, World 1!</p><div>Title #2</div><span>Hello, World 2!</span>"
    )
