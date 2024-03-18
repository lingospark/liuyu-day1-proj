# 任务描述：
# 作为一名精通Python的开发者，你的目标是创建一个能够爬取百度页面内容的爬虫。
# 任务要求：
# 1. 使用Python语言编写爬虫代码。
# 2. 确保爬虫能够有效地从百度页面提取所需信息。
# 3. 将编写好的爬虫代码上传到GitHub组织lingospark的仓库中，仓库名应为{name}-day1-proj。
# 请在代码中包含详细的注释，说明每个函数和模块的用途，以及如何运行爬虫。
# 注意事项：
# - 确保遵守百度网页的robots.txt文件规定，不要爬取禁止爬取的内容。
# - 请遵循GitHub的使用规范，不要上传包含敏感信息的文件。

import requests
from bs4 import BeautifulSoup

def get_search_results(query):
    """
    This function takes a search query, sends a request to Baidu,
    and returns the resulting HTML.

    Parameters:
    query (str): The search term to query on Baidu.

    Returns:
    str: The raw HTML of the search results.
    """

    url = "https://www.baidu.com/s?wd=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the search results: {e}")
        return None
    return response.text

def parse_search_results(html):
    """
    This function takes raw HTML and returns a list of search results.

    Parameters:
    html (str): The raw HTML from Baidu's search results.

    Returns:
    list: A list of dictionaries, each containing the title and url of a search result.
    """
    soup = BeautifulSoup(html, 'html.parser')
    search_results = []
    for result in soup.find_all('h3', {'class': 't'}):
        a = result.find('a')
        title = a.get_text()
        url = a.get('href')
        search_results.append({'title': title, 'url': url})
    return search_results

def main():
    """
    The main function of the program. It prompts the user for a search term,
    retrieves the search results from Baidu, and prints them out.
    """
    query = input("Enter a search term: ")
    html = get_search_results(query)
    if html is not None:
        results = parse_search_results(html)
        for result in results:
            print(result)

if __name__ == "__main__":
    main()