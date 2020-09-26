from converter import render_to_html


def test_render_with_simple_date_from_example():
    assert (
        render_to_html(
            [
                {"title": "Title #1", "body": "Hello, World 1!"},
                {"title": "Title #2", "body": "Hello, World 2!"},
            ]
        )
        == "<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World2!</p>"
    )
