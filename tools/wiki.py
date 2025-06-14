import wikipedia


def generate_wikipedia_reading_list(research_topic, article_titles):
    wikipedia_articles = []
    for t in article_titles:
        results = wikipedia.search(t)
        try:
            page = wikipedia.page(results[0])
            title = page.title
            url = page.url
            wikipedia_articles.append({"title": title, "url": url})
        except:
            continue
    add_to_research_reading_file(wikipedia_articles, research_topic)


def add_to_research_reading_file(articles, topic):
    with open("output/research_reading.md", "a", encoding="utf-8") as file:
        file.write(f"## {topic} \n")
        for article in articles:
            title = article["title"]
            url = article["url"]
            file.write(f"* [{title}]({url}) \n")
        file.write(f"\n\n")


generate_wikipedia_reading_list(
    "Machine Learning", ["Artificial Intelligence", "Machine Learning", "Deep Learning"]
)


def get_article(search_terms):
    article_list = []
    for search_term in search_terms:
        results = wikipedia.search(search_term)
        first_result = results[0]
        page = wikipedia.page(first_result, auto_suggest=False)
        content = page.content
        article_list.append(content)
    return article_list


get_article(["broccoli", "Ben stiller"])
