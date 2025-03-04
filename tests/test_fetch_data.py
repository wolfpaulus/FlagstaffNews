"""Test the fetch_data module."""

from fetch_data import fetch_news
import pytest


def test_fetch_news():
    """ Test the fetch_news function. """
    news = fetch_news()
    assert len(news) > 0
