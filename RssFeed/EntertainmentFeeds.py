from xml.sax import SAXParseException
import feedparser as fdp
from bs4 import BeautifulSoup as Bts


############################################### ENTERTAINMENT CLASS ########################################
class BBCRss:

    def __init__(self):
        self.content_found = ""
        self.url = "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml"
        self.entertainment_feed = fdp.parse(self.url)
        self.entry1 = self.entertainment_feed.entries[0]


    ############################################ ENTRY 1 ########################################
    def feed_link(self):
        return str(self.entry1.link)

    def title_rss(self):
        try:
            get_title = str(self.entry1.title)
        except SAXParseException:
            get_title = ""
        except KeyError:
            get_title = ""
        except IndexError:
            get_title = ""
        except Exception:
            get_title = ""

        return str(get_title)

    def content_rss(self):
        try:
            self.content_found = str(self.entry1.summary)
        except SAXParseException:
            self.content_found = ""
        except KeyError:
            self.content_found = ""
        except IndexError:
            self.content_found = ""
        except Exception:
            self.content_found = ""

        return str(self.content_found)

    def media_rss(self):
        if 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("https://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/2.5.2/bbc_news_logo.png")
            except KeyError:
                get_media = str("https://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/2.5.2/bbc_news_logo.png")
            except IndexError:
                get_media = str("https://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/2.5.2/bbc_news_logo.png")
            except Exception:
                get_media = str("https://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/2.5.2/bbc_news_logo.png")

            return str(get_media)
        else:
            return str("https://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/2.5.2/bbc_news_logo.png")


############################################### ENTERTAINMENT CLASS 2 ########################################
class IOLRss:

    def __init__(self):
        self.content_found = ""
        self.url = "http://rss.iol.io/iol/entertainment"
        self.entertainment_feed = fdp.parse(self.url)
        self.entry1 = self.entertainment_feed.entries[0]


    ############################################ ENTRY 1 ########################################
    def feed_link(self):
        return str(self.entry1.link)

    def title_rss(self):
        try:
            get_title = str(self.entry1.title)
        except SAXParseException:
            get_title = ""
        except KeyError:
            get_title = ""
        except IndexError:
            get_title = ""
        except Exception:
            get_title = ""

        return str(get_title)

    def content_rss(self):
        try:
            self.content_found = str(self.entry1.summary)
        except SAXParseException:
            self.content_found = ""
        except KeyError:
            self.content_found = ""
        except IndexError:
            self.content_found = ""
        except Exception:
            self.content_found = ""

        return str(self.content_found)

    def media_rss(self):
        if 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")
            except KeyError:
                get_media = str("https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")
            except IndexError:
                get_media = str("https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")
            except Exception:
                get_media = str(
                    "https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")

            return str(get_media)

        elif 'media_content' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_content[0]['url'])
            except SAXParseException:
                get_media = str(
                    "https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")
            except KeyError:
                get_media = str(
                    "https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")
            except IndexError:
                get_media = str(
                    "https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")
            except Exception:
                get_media = str(
                    "https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")

            return str(get_media)

        else:
            return str("https://image.iol.co.za/image/1/process/620x349?source=https://inm-baobab-prod-eu-west-1.s3.amazonaws.com/public/inm/media/2017/09/08/iol/229/IOL-breaking-news.jpg&operation=CROP&offset=81x0&resize=664x374")


############################################### ENTERTAINMENT CLASS 3 ########################################
class TheGuardienRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://www.theguardian.com/music/rss"
        self.entertainment_feed = fdp.parse(self.url)
        self.entry1 = self.entertainment_feed.entries[0]


    ############################################ ENTRY 1 ########################################
    def feed_link(self):
        return str(self.entry1.link)

    def title_rss(self):
        try:
            get_title = str(self.entry1.title)
        except SAXParseException:
            get_title = ""
        except KeyError:
            get_title = ""
        except IndexError:
            get_title = ""
        except Exception:
            get_title = ""

        return str(get_title)

    def content_rss(self):
        links = self.entry1.summary
        self.content_found = links
        page = str(self.content_found)
        soup = Bts(page, features="html.parser")
        try:
            page = soup.find('p').getText()
        except SAXParseException:
            page = ""
        except KeyError:
            page = ""
        except IndexError:
            page = ""
        except Exception:
            page = ""

        return str(page)

    def media_rss(self):
        if 'media_content' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_content[0]['url'])
            except SAXParseException:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")
            except KeyError:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")
            except IndexError:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")
            except Exception:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")

            return str(get_media)

        elif 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")
            except KeyError:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")
            except IndexError:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")
            except Exception:
                get_media = str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")

            return str(get_media)

        else:
            return str("https://d1.awsstatic.com/case-studies/600x400_Guardian_Logo.ff53f7742c12197d84de817819af20ceb973ab4d.png")


############################################### ENTERTAINMENT CLASS 4 ########################################
class TimeRss:

    def __init__(self):
        self.content_found = ""
        self.url = "http://feeds2.feedburner.com/time/entertainment"
        self.entertainment_feed = fdp.parse(self.url)
        self.entry1 = self.entertainment_feed.entries[0]


    ############################################ ENTRY 1 ########################################
    def feed_link(self):
        return str(self.entry1.link)

    def title_rss(self):
        try:
            get_title = str(self.entry1.title)
        except SAXParseException:
            get_title = ""
        except KeyError:
            get_title = ""
        except IndexError:
            get_title = ""
        except Exception:
            get_title = ""

        return str(get_title)

    def content_rss(self):
        links = self.entry1.content[0]['value']
        self.content_found = links
        page = str(self.content_found)
        soup = Bts(page, features="html.parser")
        try:
            page = soup.find('p').getText()
        except SAXParseException:
            page = ""
        except KeyError:
            page = ""
        except IndexError:
            page = ""
        except Exception:
            page = ""

        return str(page)

    def media_rss(self):
        if 'media_content' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_content[0]['url'])
            except SAXParseException:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")
            except KeyError:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")
            except IndexError:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")
            except Exception:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")

            return str(get_media)

        elif 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")
            except KeyError:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")
            except IndexError:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")
            except Exception:
                get_media = str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")

            return str(get_media)

        else:
            return str("https://s2.wp.com/wp-content/themes/vip/time2014/img/time-logo-og.png")

############################################### ENTERTAINMENT CLASS 5 ########################################
class XXLMagRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://www.xxlmag.com/feed/"
        self.entertainment_feed = fdp.parse(self.url)
        self.entry1 = self.entertainment_feed.entries[0]


    ############################################ ENTRY 1 ########################################
    def feed_link(self):
        return str(self.entry1.link)

    def title_rss(self):
        try:
            get_title = str(self.entry1.title)
        except SAXParseException:
            get_title = ""
        except KeyError:
            get_title = ""
        except IndexError:
            get_title = ""
        except Exception:
            get_title = ""

        return str(get_title)

    def content_rss(self):
        links = self.entry1.content[0]['value']
        self.content_found = links
        page = str(self.content_found)
        soup = Bts(page, features="html.parser")
        try:
            self.content_found = soup.find('p').getText()
        except SAXParseException:
            self.content_found = ""
        except KeyError:
            self.content_found = ""
        except IndexError:
            self.content_found = ""
        except Exception:
            self.content_found = ""

        return str(self.content_found)

    def media_rss(self):
        if 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("https://www.riri.com/wp-content/uploads/sites/98/2016/11/xxl-logo.jpg")
            except KeyError:
                get_media = str("https://www.riri.com/wp-content/uploads/sites/98/2016/11/xxl-logo.jpg")
            except IndexError:
                get_media = str("https://www.riri.com/wp-content/uploads/sites/98/2016/11/xxl-logo.jpg")
            except Exception:
                get_media = str("https://www.riri.com/wp-content/uploads/sites/98/2016/11/xxl-logo.jpg")

            return str(get_media)

        else:
            return str("https://www.riri.com/wp-content/uploads/sites/98/2016/11/xxl-logo.jpg")


############################################### ENTERTAINMENT CLASS 6 ########################################
class MSNBCRss:

    def __init__(self):
        self.content_found = ""
        self.url = "http://www.msnbc.com/feeds/latest"
        self.entertainment_feed = fdp.parse(self.url)
        self.entry1 = self.entertainment_feed.entries[0]


    ############################################ ENTRY 1 ########################################
    def feed_link(self):
        return str(self.entry1.link)

    def title_rss(self):
        try:
            get_title = str(self.entry1.title)
        except SAXParseException:
            get_title = ""
        except KeyError:
            get_title = ""
        except IndexError:
            get_title = ""
        except Exception:
            get_title = ""

        return str(get_title)

    def content_rss(self):
        try:
            self.content_found = self.entry1.summary
        except SAXParseException:
            self.content_found = ""
        except KeyError:
            self.content_found = ""
        except IndexError:
            self.content_found = ""
        except Exception:
            self.content_found = ""

        return str(self.content_found)


    def media_rss(self):
        if 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("https://media1.s-nbcnews.com/i/newscms/2018_21/2442291/msnbc-og-image_c986de7e1bb6ad2281723b692aa61990.png")
            except KeyError:
                get_media = str("https://media1.s-nbcnews.com/i/newscms/2018_21/2442291/msnbc-og-image_c986de7e1bb6ad2281723b692aa61990.png")
            except IndexError:
                get_media = str("https://media1.s-nbcnews.com/i/newscms/2018_21/2442291/msnbc-og-image_c986de7e1bb6ad2281723b692aa61990.png")
            except Exception:
                get_media = str("https://media1.s-nbcnews.com/i/newscms/2018_21/2442291/msnbc-og-image_c986de7e1bb6ad2281723b692aa61990.png")

            return str(get_media)

        else:
            return str("https://media1.s-nbcnews.com/i/newscms/2018_21/2442291/msnbc-og-image_c986de7e1bb6ad2281723b692aa61990.png")
