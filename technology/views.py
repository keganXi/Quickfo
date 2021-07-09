from django.shortcuts import render

from RssFeed import TechnologyFeeds
from technology.models import TheVergeDatabase
from technology.models import CnetDatabase
from technology.models import MashableDatabase
from technology.models import RecodeDatabase
from technology.models import GizmodoDatabase


# Create your views here.


def technology(request):
    collect = RssData_Collection()
    collect.Delete_Data()
    collect.DatabaseWriter()

    context = {
        'verge_data': TheVergeDatabase.objects.all().order_by('-date_published')[:6],
        'cnet_data': CnetDatabase.objects.all().order_by('-date_published')[:6],
        'mashable_data': MashableDatabase.objects.all().order_by('-date_published')[:6],
        'recode_data': RecodeDatabase.objects.all().order_by('-date_published')[:6],
        'gizmodo_data': GizmodoDatabase.objects.all().order_by('-date_published')[:6]
    }

    return render(request, "technology/TechPage.html", context)


def load_more(request):
    verge = TheVergeDatabase.objects.all().order_by('-date_published')[13:]
    for iv in verge:
        iv.delete()

    cnet = CnetDatabase.objects.all().order_by('-date_published')[13:]
    for ic in cnet:
        ic.delete()

    mash = MashableDatabase.objects.all().order_by('-date_published')[13:]
    for im in mash:
        im.delete()

    recode = RecodeDatabase.objects.all().order_by('-date_published')[13:]
    for ir in recode:
        ir.delete()

    gizmodo = GizmodoDatabase.objects.all().order_by('-date_published')[13:]
    for ig in gizmodo:
        ig.delete()


    context = {
        "verge_data": TheVergeDatabase.objects.all().order_by('-date_published')[7:],
        "cnet_data": CnetDatabase.objects.all().order_by('-date_published')[7:],
        "mashable_data": MashableDatabase.objects.all().order_by('-date_published')[7:],
        "recode_data": RecodeDatabase.objects.all().order_by('-date_published')[7:],
        "gizmodo_data": GizmodoDatabase.objects.all().order_by('-date_published')[7:],
    }
    return render(request, 'technology/TechLoadPage.html', context)


def error_404(request):
    context = {}
    return render(request, "home/404ErrorPage", context)

def error_500(request):
    context = {}
    return render(request, 'home/505ErrorPage.html', context)



class RssData_Collection:

    def __init__(self):
        # DATABASE QUERY-SET
        self.verge_feed = ""
        self.cnet_feed = ""
        self.mashable_feed = ""
        self.recode_feed = ""
        self.gizmodo_feed = ""

        # THE VERGE WEBSITE FEED
        # ENTRY 1.
        self.verge_title = TechnologyFeeds.TheVergeRss().title_rss()
        self.verge_content = TechnologyFeeds.TheVergeRss().content_rss()
        self.verge_media = TechnologyFeeds.TheVergeRss().media_rss()
        self.verge_link = TechnologyFeeds.TheVergeRss().feed_link()



        # CNET WEBSITE FEED.
        # ENTRY 1.
        self.cnet_title = TechnologyFeeds.CnetRss().title_rss()
        self.cnet_content = TechnologyFeeds.CnetRss().content_rss()
        self.cnet_media = TechnologyFeeds.CnetRss().media_rss()
        self.cnet_link = TechnologyFeeds.CnetRss().feed_link()



        # MASHABLE WEBSITE FEED.
        # ENTRY 1.
        self.mashable_title = TechnologyFeeds.MashableRss().title_rss()
        self.mashable_content = TechnologyFeeds.MashableRss().content_rss()
        self.mashable_media = TechnologyFeeds.MashableRss().media_rss()
        self.mashable_link = TechnologyFeeds.MashableRss().feed_link()



        # RECODE WEBSITE FEED.
        # ENTRY 1.
        self.recode_title = TechnologyFeeds.RecodeRss().title_rss()
        self.recode_content = TechnologyFeeds.RecodeRss().content_rss()
        self.recode_media = TechnologyFeeds.RecodeRss().media_rss()
        self.recode_link = TechnologyFeeds.RecodeRss().feed_link()



        # GIZMODO WEBSITE FEED.
        # ENTRY 1.
        self.gizmodo_title = TechnologyFeeds.GizmodoRss().title_rss()
        self.gizmodo_content = TechnologyFeeds.GizmodoRss().content_rss()
        self.gizmodo_media = TechnologyFeeds.GizmodoRss().media_rss()
        self.gizmodo_link = TechnologyFeeds.GizmodoRss().feed_link()


    def DatabaseWriter(self):
        # THE VERGE DATABASE.
        self.verge_feed = TheVergeDatabase(title_entry=self.verge_title,
                                           content_entry=self.verge_content,
                                           media_entry=self.verge_media,
                                           link_entry=self.verge_link)



        self.verge_feed.save()



        # CNET DATABASE.
        self.cnet_feed = CnetDatabase(title_entry=self.cnet_title,
                                      content_entry=self.cnet_content,
                                      media_entry=self.cnet_media,
                                      link_entry=self.cnet_link)

        self.cnet_feed.save()



        # MASHABLE DATABASE.
        self.mashable_feed = MashableDatabase(title_entry=self.mashable_title,
                                              content_entry=self.mashable_content,
                                              media_entry=self.mashable_media,
                                              link_entry=self.mashable_link)

        self.mashable_feed.save()



        # RECODE DATABASE.
        self.recode_feed = RecodeDatabase(title_entry=self.recode_title,
                                          content_entry=self.recode_content,
                                          media_entry=self.recode_media,
                                          link_entry=self.recode_link)

        self.recode_feed.save()



        # GIZMODO DATABASE.
        self.gizmodo_feed = GizmodoDatabase(title_entry=self.gizmodo_title,
                                            content_entry=self.gizmodo_content,
                                            media_entry=self.gizmodo_media,
                                            link_entry=self.gizmodo_link)
        self.gizmodo_feed.save()


    def Delete_Data(self):
        database_title = TheVergeDatabase.objects.filter(title_entry=self.verge_title)
        database_content = TheVergeDatabase.objects.filter(content_entry=self.verge_content)
        database_media = TheVergeDatabase.objects.filter(media_entry=self.verge_media)
        database_link = TheVergeDatabase.objects.filter(link_entry=self.verge_link)

        database_title.delete()
        database_content.delete()
        database_media.delete()
        database_link.delete()


        cnet_database_title = CnetDatabase.objects.filter(title_entry=self.cnet_title)
        cnet_database_content = CnetDatabase.objects.filter(content_entry=self.cnet_content)
        cnet_database_media = CnetDatabase.objects.filter(media_entry=self.cnet_media)
        cnet_database_link = CnetDatabase.objects.filter(link_entry=self.cnet_link)

        cnet_database_title.delete()
        cnet_database_content.delete()
        cnet_database_media.delete()
        cnet_database_link.delete()


        mashable_database_title = MashableDatabase.objects.filter(title_entry=self.mashable_title)
        mashable_database_content = MashableDatabase.objects.filter(content_entry=self.mashable_content)
        mashable_database_media = MashableDatabase.objects.filter(media_entry=self.mashable_media)
        mashable_database_link = MashableDatabase.objects.filter(link_entry=self.mashable_link)

        mashable_database_title.delete()
        mashable_database_content.delete()
        mashable_database_media.delete()
        mashable_database_link.delete()


        recode_database_title = RecodeDatabase.objects.filter(title_entry=self.recode_title)
        recode_database_content = RecodeDatabase.objects.filter(content_entry=self.recode_content)
        recode_database_media = RecodeDatabase.objects.filter(media_entry=self.recode_media)
        recode_database_link = RecodeDatabase.objects.filter(link_entry=self.recode_link)

        recode_database_title.delete()
        recode_database_content.delete()
        recode_database_media.delete()
        recode_database_link.delete()


        giz_database_title = GizmodoDatabase.objects.filter(title_entry=self.gizmodo_title)
        giz_database_content = GizmodoDatabase.objects.filter(content_entry=self.gizmodo_content)
        giz_database_media = GizmodoDatabase.objects.filter(media_entry=self.gizmodo_media)
        giz_database_link = GizmodoDatabase.objects.filter(link_entry=self.gizmodo_link)

        giz_database_title.delete()
        giz_database_content.delete()
        giz_database_media.delete()
        giz_database_link.delete()

