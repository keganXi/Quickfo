from django.shortcuts import render
from django.http import Http404

from home.models import TheVergeDatabase
from home.models import TheIndependentDatabase
from home.models import MSNBCDatabase
from home.models import XXLMagDatabase

from RssFeed import TechnologyFeeds
from RssFeed import EntertainmentFeeds
from RssFeed import SportsFeeds

# Create your views here.


def homepage(request):

    collect = RssData_Collection()
    collect.Delete_Data()
    collect.DatabaseWriter()


    context = {
        "verge_data": TheVergeDatabase.objects.all().order_by('-date_published')[:6],
        "theindependent_data": TheIndependentDatabase.objects.all().order_by('-date_published')[:6],
        "msnbc_data": MSNBCDatabase.objects.all().order_by('-date_published')[:6],
        "xxlmag_data": XXLMagDatabase.objects.all().order_by('-date_published')[:6]
    }
    return render(request, 'home/HomePage.html', context)


def load_more(request):
    verge = TheVergeDatabase.objects.all().order_by('-date_published')[13:]
    for iv in verge:
        iv.delete()

    independent = TheIndependentDatabase.objects.all().order_by('-date_published')[13:]
    for id in independent:
        id.delete()

    msnbc = MSNBCDatabase.objects.all().order_by('-date_published')[13:]
    for im in msnbc:
        im.delete()

    xxl = XXLMagDatabase.objects.all().order_by('-date_published')[13:]
    for ix in xxl:
        ix.delete()


    context = {
        "verge_data": TheVergeDatabase.objects.all().order_by('-date_published')[7:],
        "theindependent_data": TheIndependentDatabase.objects.all().order_by('-date_published')[7:],
        "msnbc_data": MSNBCDatabase.objects.all().order_by('-date_published')[7:],
        "xxlmag_data": XXLMagDatabase.objects.all().order_by('-date_published')[7:]
    }
    return render(request, 'home/LoadPage.html', context)



class RssData_Collection:

    def __init__(self):
        # DATABASE QUERY-SET
        self.theverge_feed = ""
        self.msnbc_feed = ""
        self.theindependent_feed = ""
        self.xxlmag_feed = ""

        # THE THE VERGE WEBSITE FEED
        # ENTRY 1.
        self.theverge_title = TechnologyFeeds.TheVergeRss().title_rss()
        self.theverge_content = TechnologyFeeds.TheVergeRss().content_rss()
        self.theverge_media = TechnologyFeeds.TheVergeRss().media_rss()
        self.theverge_link = TechnologyFeeds.TheVergeRss().feed_link()



        # MSNBC WEBSITE FEED.
        # ENTRY 1.
        self.msnbc_title = EntertainmentFeeds.MSNBCRss().title_rss()
        self.msnbc_content = EntertainmentFeeds.MSNBCRss().content_rss()
        self.msnbc_media = EntertainmentFeeds.MSNBCRss().media_rss()
        self.msnbc_link = EntertainmentFeeds.MSNBCRss().feed_link()



        # THE INDEPENDENT WEBSITE FEED.
        # ENTRY 1.
        self.theindependent_title = SportsFeeds.TheIndependentRss().title_rss()
        self.theindependent_content = SportsFeeds.TheIndependentRss().content_rss()
        self.theindependent_media = SportsFeeds.TheIndependentRss().media_rss()
        self.theindependent_link = SportsFeeds.TheIndependentRss().feed_link()



        # XXL MAG WEBSITE FEED.
        # ENTRY 1.
        self.xxlmag_title = EntertainmentFeeds.XXLMagRss().title_rss()
        self.xxlmag_content = EntertainmentFeeds.XXLMagRss().content_rss()
        self.xxlmag_media = EntertainmentFeeds.XXLMagRss().media_rss()
        self.xxlmag_link = EntertainmentFeeds.XXLMagRss().feed_link()



    def DatabaseWriter(self):
        # THE VERGE DATABASE.
        self.theverge_feed = TheVergeDatabase(title_entry=self.theverge_title,
                                              content_entry=self.theverge_content,
                                              media_entry=self.theverge_media,
                                              link_entry=self.theverge_link)



        self.theverge_feed.save()



        # MSNBC DATABASE.
        self.msnbc_feed = MSNBCDatabase(title_entry=self.msnbc_title,
                                        content_entry=self.msnbc_content,
                                        media_entry=self.msnbc_media,
                                        link_entry=self.msnbc_link)

        self.msnbc_feed.save()



        # THE INDEPENDENT DATABASE.
        self.theindependent_feed = TheIndependentDatabase(title_entry=self.theindependent_title,
                                                          content_entry=self.theindependent_content,
                                                          media_entry=self.theindependent_media,
                                                          link_entry=self.theindependent_link)

        self.theindependent_feed.save()



        # XXL MAG DATABASE.
        self.xxlmag_feed = XXLMagDatabase(title_entry=self.xxlmag_title,
                                          content_entry=self.xxlmag_content,
                                          media_entry=self.xxlmag_media,
                                          link_entry=self.xxlmag_link)

        self.xxlmag_feed.save()



    def Delete_Data(self):
        database_title = TheVergeDatabase.objects.filter(title_entry=self.theverge_title)
        database_content = TheVergeDatabase.objects.filter(content_entry=self.theverge_content)
        database_media = TheVergeDatabase.objects.filter(media_entry=self.theverge_media)
        database_link = TheVergeDatabase.objects.filter(link_entry=self.theverge_link)

        database_title.delete()
        database_content.delete()
        database_media.delete()
        database_link.delete()


        msnbc_database_title = MSNBCDatabase.objects.filter(title_entry=self.msnbc_title)
        msnbc_database_content = MSNBCDatabase.objects.filter(content_entry=self.msnbc_content)
        msnbc_database_media = MSNBCDatabase.objects.filter(media_entry=self.msnbc_media)
        msnbc_database_link = MSNBCDatabase.objects.filter(link_entry=self.msnbc_link)

        msnbc_database_title.delete()
        msnbc_database_content.delete()
        msnbc_database_media.delete()
        msnbc_database_link.delete()


        theindependent_database_title = TheIndependentDatabase.objects.filter(title_entry=self.theindependent_title)
        theindependent_database_content = TheIndependentDatabase.objects.filter(content_entry=self.theindependent_content)
        theindependent_database_media = TheIndependentDatabase.objects.filter(media_entry=self.theindependent_media)
        theindependent_database_link = TheIndependentDatabase.objects.filter(link_entry=self.theindependent_link)

        theindependent_database_title.delete()
        theindependent_database_content.delete()
        theindependent_database_media.delete()
        theindependent_database_link.delete()


        xxlmag_database_title = XXLMagDatabase.objects.filter(title_entry=self.xxlmag_title)
        xxlmag_database_content = XXLMagDatabase.objects.filter(content_entry=self.xxlmag_content)
        xxlmag_database_media = XXLMagDatabase.objects.filter(media_entry=self.xxlmag_media)
        xxlmag_database_link = XXLMagDatabase.objects.filter(link_entry=self.xxlmag_link)

        xxlmag_database_title.delete()
        xxlmag_database_content.delete()
        xxlmag_database_media.delete()
        xxlmag_database_link.delete()


