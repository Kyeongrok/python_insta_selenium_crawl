from libs.crawler import crawl

url = "https://www.instagram.com/explore/tags/%EB%B0%9C%EB%A0%88/"

pageString = crawl(url)
print(pageString)