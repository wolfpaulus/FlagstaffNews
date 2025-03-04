# FlagstaffNews

Prep:
Find a web service.
E.g.: RSS Feed: https://www.abc15.com/news/region-northern-az/flagstaff.rss
Add a LICENSE file


1. Create a new repo on github
2. Clone the repo to you computer
2.1 E.g. in VSCode new window ..clone
2.2 copy you .vscode/settints.json
3. create src and tests directories
4. create ./requirements.txt and ./tests/requirements,txt files
  e.g.: streamlit
  e.g.: pytest
5. create a pytest.ini file
  # pytest.ini
  [pytest]
  pythonpath = src
  testpaths = tests
6. Crete a virtual environment and install the requirements
7. Write a test that asserts you are fetching data
8. Implement the code that fetches the data
9. run pytest
10. build the UI