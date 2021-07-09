from xml.sax import SAXParseException
import feedparser as fdp
from bs4 import BeautifulSoup as Bts


############################################### TECH FEED 1 ###################################
class TheVergeRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://www.theverge.com/tech/rss/index.xml"
        self.tech_feed = fdp.parse(self.url)
        self.entry1 = self.tech_feed.entries[0]

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
        soup = Bts(self.entry1.summary, features="html.parser")
        image_img = soup.find('img')
        image_href = soup.find('a')
        if 'img' or image_img['src'] in self.entry1.summary:
            try:
                get_media = str(image_img['src'])
            except SAXParseException:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")
            except KeyError:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")
            except IndexError:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")
            except Exception:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")

            return str(get_media)

        elif image_href['href'] in self.entry1.summary:
            try:
                get_media = str(image_href['href'])
            except SAXParseException:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")
            except KeyError:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")
            except IndexError:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")
            except Exception:
                get_media = str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")

            return str(get_media)
        else:
            return str("https://image4.owler.com/logo/the-verge_owler_20170323_105118_original.png")


################################################# TECH FEED 2 ###################################################
class CnetRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://www.cnet.com/rss/news/"
        self.tech_feed = fdp.parse(self.url)
        self.entry1 = self.tech_feed.entries[0]

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
        try:
            page = str(self.content_found)
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
        if 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")
            except KeyError:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")
            except IndexError:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")
            except Exception:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")

            return str(get_media)
        elif 'media-content' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_content[0]['url'])
            except SAXParseException:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")
            except KeyError:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")
            except IndexError:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")
            except Exception:
                get_media = str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")

            return str(get_media)
        else:
            return str("https://www.kaporcenter.org/wp-content/uploads/2017/07/CNET.png")


################################################# TECH FEED 3 ###################################################
class MashableRss:

    def __init__(self):
        self.content_found = ""
        self.url = "http://feeds.mashable.com/Mashable"
        self.tech_feed = fdp.parse(self.url)
        self.entry1 = self.tech_feed.entries[0]

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
        soup = Bts(self.entry1.content[0]['value'], features="html.parser")
        image_url = soup.find('img')['src']
        if image_url:
            try:
                get_media = str(image_url)
            except SAXParseException:
                get_media = str("https://i.kym-cdn.com/entries/icons/original/000/016/241/Mashable-large.jpg")
            except KeyError:
                get_media = str("https://i.kym-cdn.com/entries/icons/original/000/016/241/Mashable-large.jpg")
            except IndexError:
                get_media = str("https://i.kym-cdn.com/entries/icons/original/000/016/241/Mashable-large.jpg")
            except Exception:
                get_media = str("https://i.kym-cdn.com/entries/icons/original/000/016/241/Mashable-large.jpg")

            return str(get_media)

        elif 'media_thumbnail' in self.entry1.keys():
            return str(self.entry1.media_thumbnail[0]['url'])

        else:
            return str("https://i.kym-cdn.com/entries/icons/original/000/016/241/Mashable-large.jpg")


################################################# TECH FEED 4 ###################################################
class RecodeRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://www.vox.com/rss/index.xml"
        self.tech_feed = fdp.parse(self.url)
        self.entry1 = self.tech_feed.entries[0]

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
        try:
            page = str(self.content_found)
            soup = Bts(page, features="html.parser")
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
        soup = Bts(self.entry1.content[0]['value'], features="html.parser")
        image_url = soup.find('img')['src']
        if image_url:
            try:
                get_media = str(image_url)
            except SAXParseException:
                get_media = str("https://cdn.vox-cdn.com/thumbor/ZQAssWEA6rXB4f49avxPGc84TzI=/17x0:542x350/1200x800/filters:focal(17x0:542x350)/cdn.vox-cdn.com/assets/3794111/recode.jpg")
            except KeyError:
                get_media = str("https://cdn.vox-cdn.com/thumbor/ZQAssWEA6rXB4f49avxPGc84TzI=/17x0:542x350/1200x800/filters:focal(17x0:542x350)/cdn.vox-cdn.com/assets/3794111/recode.jpg")
            except IndexError:
                get_media = str("https://cdn.vox-cdn.com/thumbor/ZQAssWEA6rXB4f49avxPGc84TzI=/17x0:542x350/1200x800/filters:focal(17x0:542x350)/cdn.vox-cdn.com/assets/3794111/recode.jpg")
            except Exception:
                get_media = str("https://cdn.vox-cdn.com/thumbor/ZQAssWEA6rXB4f49avxPGc84TzI=/17x0:542x350/1200x800/filters:focal(17x0:542x350)/cdn.vox-cdn.com/assets/3794111/recode.jpg")

            return str(get_media)

        elif 'media_thumbnail' in self.entry1.keys():
            return str(self.entry1.media_thumbnail[0]['url'])

        else:
            return str("https://cdn.vox-cdn.com/thumbor/ZQAssWEA6rXB4f49avxPGc84TzI=/17x0:542x350/1200x800/filters:focal(17x0:542x350)/cdn.vox-cdn.com/assets/3794111/recode.jpg")

################################################# TECH FEED 5 ###################################################
class GizmodoRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://gizmodo.com/rss"
        self.tech_feed = fdp.parse(self.url)
        self.entry1 = self.tech_feed.entries[0]

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
        try:
            page = str(self.content_found)
            soup = Bts(page, features="html.parser")
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
        soup = Bts(self.entry1.summary, features="html.parser")
        image_url = soup.find('img')['src']
        if image_url:
            try:
                get_media = str(image_url)
            except SAXParseException:
                get_media = str("https://www.niemanlab.org/images/gizmodo-media-700x400.jpg")
            except KeyError:
                get_media = str("https://www.niemanlab.org/images/gizmodo-media-700x400.jpg")
            except IndexError:
                get_media = str("https://www.niemanlab.org/images/gizmodo-media-700x400.jpg")
            except Exception:
                get_media = str("https://www.niemanlab.org/images/gizmodo-media-700x400.jpg")

            return str(get_media)

        elif 'media_thumbnail' in self.entry1.keys():
            return str(self.entry1.media_thumbnail[0]['url'])

        else:
            return str("https://www.niemanlab.org/images/gizmodo-media-700x400.jpg")

