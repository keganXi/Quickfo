from xml.sax import SAXParseException
import feedparser as fdp
from bs4 import BeautifulSoup as Bts


############################################### SPORTS CLASS ########################################
class FoxSportsRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU"
        self.sports_feed = fdp.parse(self.url)
        self.entry1 = self.sports_feed.entries[0]


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
        if 'links' in self.entry1.keys():
            try:
                get_media = str(self.entry1.links[1]['href'])
            except SAXParseException:
                get_media = str("https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except KeyError:
                get_media = str("https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except IndexError:
                get_media = str("https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except Exception:
                get_media = str("https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")

            return str(get_media)
        elif 'media_thumbnail' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except KeyError:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except IndexError:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except Exception:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")

            return str(get_media)
        elif 'media_content' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_content[0]['url'])
            except SAXParseException:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except KeyError:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except IndexError:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")
            except Exception:
                get_media = str(
                    "https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")

            return str(get_media)

        else:
            return str("https://www.grandprix.com.au/sites/default/files/styles/main_visual_element_transp_image_default/public/partner/image/logo/Untitled-1.png")


####################################################### SPORTS CLASS 2 ################################################
class TheGuardienRss:

    def __init__(self):
        self.content_found = ""
        self.url = "https://www.theguardian.com/uk/sport/rss"
        self.sports_feed = fdp.parse(self.url)
        self.entry1 = self.sports_feed.entries[0]


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


################################################ SPORTS CLASS 3 #######################################################
class BBCSportRss:

    def __init__(self):
        self.content_found = ""
        self.url = "http://feeds.bbci.co.uk/sport/rss.xml?edition=uk"
        self.sports_feed = fdp.parse(self.url)
        self.entry1 = self.sports_feed.entries[0]


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
                get_media = str("https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")
            except KeyError:
                get_media = str("https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")
            except IndexError:
                get_media = str("https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")
            except Exception:
                get_media = str("https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")

            return str(get_media)

        elif 'media_content' in self.entry1.keys():
            try:
                get_media = str(self.entry1.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str(
                    "https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")
            except KeyError:
                get_media = str(
                    "https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")
            except IndexError:
                get_media = str(
                    "https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")
            except Exception:
                get_media = str(
                    "https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")

            return str(get_media)
        else:
            return str("https://www.newswhip.com/wp-content/uploads/2016/02/Images-for-first-page-articles_Page_30.jpg")


###################################################### SPORTS CLASS 4 ################################################
class TheIndependentRss:

    def __init__(self):
        self.content_found = ""
        self.url = "http://www.independent.co.uk/sport/rss"
        self.sports_feed = fdp.parse(self.url)
        self.entry1 = self.sports_feed.entries[0]


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
        png_link = self.entry1
        if 'media_thumbnail' in png_link.keys():
            try:
                get_media = str(png_link.media_thumbnail[0]['url'])
            except SAXParseException:
                get_media = str("http://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")
            except KeyError:
                get_media = str("http://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")
            except IndexError:
                get_media = str(
                    "http://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")
            except Exception:
                get_media = str(
                    "http://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")

            return str(get_media)

        elif 'media_content' in png_link.keys():
            try:
                get_media = str(png_link.media_content[0]['url'])
            except SAXParseException:
                get_media = str("http://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")
            except KeyError:
                get_media = str("hhttp://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")
            except IndexError:
                get_media = str(
                    "hhttp://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")
            except Exception:
                get_media = str(
                    "http://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")

            return str(get_media)

        else:
            return str("http://winonmarkets.net/wp/wp-content/uploads/2011/04/the-independent.jpg")
