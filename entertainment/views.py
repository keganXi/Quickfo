from django.shortcuts import render
from RssFeed import EntertainmentFeeds
from .models import BBCDatabase
from .models import IOLDatabase
from .models import TheGuardianDatabase
from .models import TimeDatabase
from .models import XXLMagDatabase

# Create your views here.


def entertainment(request):
    collect = RssData_Collection()
    collect.Delete_Data()
    collect.DatabaseWriter()

    context = {
        'bbc_data': BBCDatabase.objects.all().order_by('-date_published')[:6],
        'iol_data': IOLDatabase.objects.all().order_by('-date_published')[:6],
        'theguardian_data': TheGuardianDatabase.objects.all().order_by('-date_published')[:6],
        'time_data': TimeDatabase.objects.all().order_by('-date_published')[:6],
        'xxlmag_data': XXLMagDatabase.objects.all().order_by('-date_published')[:6]
    }
    return render(request, "entertainment/EntertainmentPage.html", context)


def load_more(request):
    bbc = BBCDatabase.objects.all().order_by('-date_published')[13:]
    for ib in bbc:
        ib.delete()

    iol = IOLDatabase.objects.all().order_by('-date_published')[13:]
    for ii in iol:
        ii.delete()

    theguardian = TheGuardianDatabase.objects.all().order_by('-date_published')[13:]
    for ig in theguardian:
        ig.delete()

    time = TimeDatabase.objects.all().order_by('-date_published')[13:]
    for it in time:
        it.delete()

    xxlmag = XXLMagDatabase.objects.all().order_by('-date_published')[13:]
    for ix in xxlmag:
        ix.delete()


    context = {
        "bbc_data": BBCDatabase.objects.all().order_by('-date_published')[7:],
        "iol_data": IOLDatabase.objects.all().order_by('-date_published')[7:],
        "theguardian_data": TheGuardianDatabase.objects.all().order_by('-date_published')[7:],
        "time_data": TimeDatabase.objects.all().order_by('-date_published')[7:],
        "xxlmag_data": XXLMagDatabase.objects.all().order_by('-date_published')[7:],
    }
    return render(request, 'entertainment/EntertainmentLoadPage.html', context)


class RssData_Collection:

    def __init__(self):
        # DATABASE QUERY-SET
        self.bbc_feed = ""
        self.iol_feed = ""
        self.theguardian_feed = ""
        self.time_feed = ""
        self.xxlmag_feed = ""

        # THE NEWS24 WEBSITE FEED
        # ENTRY 1.
        self.bbc_title = EntertainmentFeeds.BBCRss().title_rss()
        self.bbc_content = EntertainmentFeeds.BBCRss().content_rss()
        self.bbc_media = EntertainmentFeeds.BBCRss().media_rss()
        self.bbc_link = EntertainmentFeeds.BBCRss().feed_link()



        # SKYNEWS WEBSITE FEED.
        # ENTRY 1.
        self.iol_title = EntertainmentFeeds.IOLRss().title_rss()
        self.iol_content = EntertainmentFeeds.IOLRss().content_rss()
        self.iol_media = EntertainmentFeeds.IOLRss().media_rss()
        self.iol_link = EntertainmentFeeds.IOLRss().feed_link()



        # MSNBC WEBSITE FEED.
        # ENTRY 1.
        self.theguardian_title = EntertainmentFeeds.TheGuardienRss().title_rss()
        self.theguardian_content = EntertainmentFeeds.TheGuardienRss().content_rss()
        self.theguardian_media = EntertainmentFeeds.TheGuardienRss().media_rss()
        self.theguardian_link = EntertainmentFeeds.TheGuardienRss().feed_link()



        # THE GUARDIAN WEBSITE FEED.
        # ENTRY 1.
        self.time_title = EntertainmentFeeds.TimeRss().title_rss()
        self.time_content = EntertainmentFeeds.TimeRss().content_rss()
        self.time_media = EntertainmentFeeds.TimeRss().media_rss()
        self.time_link = EntertainmentFeeds.TimeRss().feed_link()



        # BBC WEBSITE FEED.
        # ENTRY 1.
        self.xxlmag_title = EntertainmentFeeds.XXLMagRss().title_rss()
        self.xxlmag_content = EntertainmentFeeds.XXLMagRss().content_rss()
        self.xxlmag_media = EntertainmentFeeds.XXLMagRss().media_rss()
        self.xxlmag_link = EntertainmentFeeds.XXLMagRss().feed_link()


    def DatabaseWriter(self):
        # THE BBC DATABASE.
        self.bbc_feed = BBCDatabase(title_entry=self.bbc_title,
                                    content_entry=self.bbc_content,
                                    media_entry=self.bbc_media,
                                    link_entry=self.bbc_link)



        self.bbc_feed.save()



        # IOL DATABASE.
        self.iol_feed = IOLDatabase(title_entry=self.iol_title,
                                    content_entry=self.iol_content,
                                    media_entry=self.iol_media,
                                    link_entry=self.iol_link)

        self.iol_feed.save()



        # THE GUARDIAN DATABASE.
        self.theguardian_feed = TheGuardianDatabase(title_entry=self.theguardian_title,
                                                    content_entry=self.theguardian_content,
                                                    media_entry=self.theguardian_media,
                                                    link_entry=self.theguardian_link)

        self.theguardian_feed.save()



        # THE TIME DATABASE.
        self.time_feed = TimeDatabase(title_entry=self.time_title,
                                      content_entry=self.time_content,
                                      media_entry=self.time_media,
                                      link_entry=self.time_link)

        self.time_feed.save()



        # XXLMAG DATABASE.
        self.xxlmag_feed = XXLMagDatabase(title_entry=self.xxlmag_title,
                                          content_entry=self.xxlmag_content,
                                          media_entry=self.xxlmag_media,
                                          link_entry=self.xxlmag_link)
        self.xxlmag_feed.save()


    def Delete_Data(self):
        database_title = BBCDatabase.objects.filter(title_entry=self.bbc_title)
        database_content = BBCDatabase.objects.filter(content_entry=self.bbc_content)
        database_media = BBCDatabase.objects.filter(media_entry=self.bbc_media)
        database_link = BBCDatabase.objects.filter(link_entry=self.bbc_link)

        database_title.delete()
        database_content.delete()
        database_media.delete()
        database_link.delete()


        iol_database_title = IOLDatabase.objects.filter(title_entry=self.iol_title)
        iol_database_content = IOLDatabase.objects.filter(content_entry=self.iol_content)
        iol_database_media = IOLDatabase.objects.filter(media_entry=self.iol_media)
        iol_database_link = IOLDatabase.objects.filter(link_entry=self.iol_link)

        iol_database_title.delete()
        iol_database_content.delete()
        iol_database_media.delete()
        iol_database_link.delete()


        theguardian_database_title = TheGuardianDatabase.objects.filter(title_entry=self.theguardian_title)
        theguardian_database_content = TheGuardianDatabase.objects.filter(content_entry=self.theguardian_content)
        theguardian_database_media = TheGuardianDatabase.objects.filter(media_entry=self.theguardian_media)
        theguardian_database_link = TheGuardianDatabase.objects.filter(link_entry=self.theguardian_link)

        theguardian_database_title.delete()
        theguardian_database_content.delete()
        theguardian_database_media.delete()
        theguardian_database_link.delete()


        time_database_title = TimeDatabase.objects.filter(title_entry=self.time_title)
        time_database_content = TimeDatabase.objects.filter(content_entry=self.time_content)
        time_database_media = TimeDatabase.objects.filter(media_entry=self.time_media)
        time_database_link = TimeDatabase.objects.filter(link_entry=self.time_link)

        time_database_title.delete()
        time_database_content.delete()
        time_database_media.delete()
        time_database_link.delete()


        xxlmag_database_title = XXLMagDatabase.objects.filter(title_entry=self.xxlmag_title)
        xxlmag_database_content = XXLMagDatabase.objects.filter(content_entry=self.xxlmag_content)
        xxlmag_database_media = XXLMagDatabase.objects.filter(media_entry=self.xxlmag_media)
        xxlmag_database_link = XXLMagDatabase.objects.filter(link_entry=self.xxlmag_link)

        xxlmag_database_title.delete()
        xxlmag_database_content.delete()
        xxlmag_database_media.delete()
        xxlmag_database_link.delete()

