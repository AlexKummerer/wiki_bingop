import pytest
import wikipedia_api
import wikipedia

def test_extract_title_from_url():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    title = wikipedia_api.extract_title_from_url(url)
    assert title == "Python_(programming_language)"

def test_set_wikipedia_language(monkeypatch):
    def mock_set_lang(language):
        assert language == "es"

    monkeypatch.setattr(wikipedia, "set_lang", mock_set_lang)
    url = "https://es.wikipedia.org/wiki/Python"
    wikipedia_api.set_wikipedia_language(url)

def test_validate_category_from_url(monkeypatch):
    def mock_get_page_categories(title):
        return ["Programming languages", "Python"]

    monkeypatch.setattr(wikipedia_api, 'get_page_categories', mock_get_page_categories)

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    bingo_df = ["Programming languages"]
    valid, categories = wikipedia_api.validate_category_from_url(url, bingo_df)
    assert valid == True
    assert "Programming languages" in categories
