# 任务描述：
# 作为一名精通Python的开发者，你的目标是创建一个能够爬取百度页面内容的爬虫。
# 任务要求：
# 1. 使用Python语言编写爬虫代码。
# 2. 确保爬虫能够有效地从百度页面提取所需信息。
# 3. 将编写好的爬虫代码上传到GitHub组织lingospark的仓库中，仓库名应为{name}-day1-proj。
# 4. 爬虫代码应命名为main函数，目标URL作为参数传入。
# 5. 在if __name__ == "__main__"中调用main函数，并传入百度的URL。
# 6. 函数应使用类型提示（type hint），并包含文档字符串（documentation），解释输入参数和函数功能。
# 注意事项：
# - 确保遵守百度网页的robots.txt文件规定，不要爬取禁止爬取的内容。
# - 请遵循GitHub的使用规范，不要上传包含敏感信息的文件。
# - 在编写代码时，应考虑代码的可读性和可维护性。

# 示例代码结构：
"""
def main(target_url: str) -> None:
    '''
    主函数，用于爬取指定URL的页面内容。

    参数:
    target_url: str - 要爬取的目标网页的URL。

    功能描述:
    该函数接收一个URL作为参数，访问并爬取该URL的内容，然后将结果输出或保存。
    '''
    # 爬虫代码逻辑...
    pass

if __name__ == "__main__":
    baidu_url = 'https://www.baidu.com'  # 百度的URL
    main(baidu_url)
"""
# 请将上述代码结构作为参考，根据实际情况进行调整和完善。

import requests
from bs4 import BeautifulSoup

def get_search_results(query: str) -> str:
    """
    此函数接受一个搜索查询，向百度发送请求，并返回得到的HTML结果。

    参数:
    query (str): 在百度上查询的搜索词。

    返回值:
    str: 搜索结果的原始HTML。
    """

    url = "https://www.baidu.com/s?wd=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"获取搜索结果时出现错误: {e}")
        return None
    return response.text


def parse_search_results(html: str) -> list:
    """
    此函数接受原始HTML，并返回搜索结果列表。

    参数:
    html (str): 百度搜索结果的原始HTML。

    返回值:
    list: 一个字典列表，每个字典包含搜索结果的标题和url。
    """
    soup = BeautifulSoup(html, 'html.parser')
    search_results = []
    for result in soup.find_all('h3', {'class': 't'}):
        a = result.find('a')
        title = a.get_text()
        url = a.get('href')
        search_results.append({'title': title, 'url': url})
    return search_results


def main(url: str):
    """
    程序的主函数。提示用户输入搜索词，从百度检索搜索结果，然后打印出来。
    """
    query = input("请输入搜索词: ")
    html = get_search_results(query)
    if html is not None:
        results = parse_search_results(html)
        for result in results:
            print(result)


if __name__ == "__main__":
    main("https://www.baidu.com")
