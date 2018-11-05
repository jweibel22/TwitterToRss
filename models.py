

class Item:

    def __init__(self, id, title, url, created_at):
        self.id = id
        self.title = title
        self.url = url
        self.created_at = created_at
        self.item_template = '<item>'\
'<title>%s</title>'\
'<link>%s</link>'\
'<description>%s</description>'\
'<guid isPermaLink="false">%s</guid>'\
'<pubDate>%s</pubDate>'\
'</item>'

    def to_string(self):
        return self.item_template % (self.title.encode('utf-8'), self.url.encode('utf-8'), "", self.id, self.created_at)


class Feed:

    def __init__(self, title, items):
        self.title = title
        self.items = items
        self.rss_template = '<?xml version="1.0" encoding="utf-8" ?><rss version="2.0" xml:base="https://identity-jweibel-88507.appspot.com/rss/bbcdailynews" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom">' \
                   '<channel>' \
                   '<title>{title}</title>' \
                   '<link>https://identity-jweibel-88507.appspot.com/rss/bbcdailynews</link>' \
                   '<description> </description>' \
                   '<language>da</language>' \
                   '<atom:link href = "https://identity-jweibel-88507.appspot.com/rss/bbcdailynews" rel="self" type="application/rss+xml"/>' \
                   '{items}' \
                   '</channel>' \
                   '</rss>'

    def to_string(self):
        xxx = list(map(lambda item: item.to_string(), self.items))
        return self.rss_template.format(title=self.title, items="\n".join(xxx))
