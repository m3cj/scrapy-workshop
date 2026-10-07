import sqlite3


class QuotetutorialPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS quotes_tb (
                title TEXT,
                author TEXT,
                tags TEXT
            )
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        title = item.get("title", "")
        author = item.get("author", "")
        tags = item.get("tags", "")

        title_str = " ".join(title) if isinstance(title, list) else str(title)
        author_str = " ".join(author) if isinstance(author, list) else str(author)
        tags_str = ", ".join(tags) if isinstance(tags, list) else str(tags)

        self.curr.execute(
            "INSERT INTO quotes_tb VALUES (?, ?, ?)",
            (title_str, author_str, tags_str)
        )
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()
