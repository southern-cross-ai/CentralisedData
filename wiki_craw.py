import wikipediaapi

# 自定义的 User-Agent 字符串
user_agent = "MyWikipediaCrawler/1.0 (u766@anu.edu.au)"

# 创建维基百科API对象，并指定 User-Agent
wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)

def get_articles_recursive(page, max_depth, current_depth=0):
    if current_depth > max_depth:
        return {}

    articles = {page.title: page.text}

    # 递归获取链接的内容
    for title, link in page.links.items():
        if "Australia" in title and current_depth < max_depth:
            linked_page = wiki_wiki.page(link.title)
            if linked_page.exists():
                print(f"{'  ' * current_depth}Crawling: {linked_page.title} at depth {current_depth + 1}")
                articles.update(get_articles_recursive(linked_page, max_depth, current_depth + 1))
    
    return articles

def save_articles_to_files(articles, directory="australia_articles"):
    import os

    if not os.path.exists(directory):
        os.makedirs(directory)

    for title, content in articles.items():
        filename = os.path.join(directory, f"{title.replace('/', '_')}.txt")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
            print(f"Saved: {filename}")

def main():
    search_term = "Australia"
    start_page = wiki_wiki.page(search_term)

    if not start_page.exists():
        print(f"No article found for {search_term}")
        return

    max_depth = 1  # 设置爬取深度
    articles = get_articles_recursive(start_page, max_depth)
    if articles:
        save_articles_to_files(articles)

if __name__ == "__main__":
    main()
