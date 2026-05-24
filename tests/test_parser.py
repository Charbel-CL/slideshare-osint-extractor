from app.parser import parse_search_results


def test_parse_search_results():

    html = """
    <div class="search-result">
        <a class="title"
           href="https://www.slideshare.net/test1">
           Test Title
        </a>

        <span class="author">
            Test Author
        </span>

        <p class="description">
            Test Description
        </p>

        <span class="views">
            1234
        </span>

        <span class="upload-date">
            2026-05-24
        </span>
    </div>
    """

    results = parse_search_results(
        html=html,
        page=1
    )

    assert len(results) == 1

    assert results[0].title == "Test Title"

    assert results[0].author == "Test Author"