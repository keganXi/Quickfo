from django.shortcuts import render
from RssFeed import SportsFeeds
from .models import FoxSportsDatabase
from .models import TheGuardianDatabase
from .models import BBCSportsDatabase
from .models import TheIndependentDatabase

# Create your views here.


def sports(request):
    collect = RssData_Collection()
    collect.Delete_Data()
    collect.DatabaseWriter()

    context = {
        'foxsports_data': FoxSportsDatabase.objects.all().order_by('-date_published')[:6],
        'theguardian_data': TheGuardianDatabase.objects.all().order_by('-date_published')[:6],
        'bbcsports_data': BBCSportsDatabase.objects.all().order_by('-date_published')[:6],
        'theindependent_data': TheIndependentDatabase.objects.all().order_by('-date_published')[:6]
    }
    return render(request, "sports/SportsPage.html", context)



def load_more(request):
    fox = FoxSportsDatabase.objects.all().order_by('-date_published')[13:]
    for ifox in fox:
        ifox.delete()

    theguardian = TheGuardianDatabase.objects.all().order_by('-date_published')[13:]
    for ig in theguardian:
        ig.delete()

    bbcsports = BBCSportsDatabase.objects.all().order_by('-date_published')[13:]
    for ib in bbcsports:
        ib.delete()

    theindependent = TheIndependentDatabase.objects.all().order_by('-date_published')[13:]
    for it in theindependent:
        it.delete()


    context = {
        "foxsports_data": FoxSportsDatabase.objects.all().order_by('-date_published')[7:],
        "theguardian_data": TheGuardianDatabase.objects.all().order_by('-date_published')[7:],
        "bbcsports_data": BBCSportsDatabase.objects.all().order_by('-date_published')[7:],
        "theindependent_data": TheIndependentDatabase.objects.all().order_by('-date_published')[7:],
    }
    return render(request, 'sports/SportsLoadPage.html', context)



class RssData_Collection:

    def __init__(self):
        # DATABASE QUERY-SET
        self.foxsports_feed = ""
        self.theguardian_feed = ""
        self.bbcsports_feed = ""
        self.theindependent_feed = ""

        # THE FOX SPORTS WEBSITE FEED
        # ENTRY 1.
        self.foxsports_title = SportsFeeds.FoxSportsRss().title_rss()
        self.foxsports_content = SportsFeeds.FoxSportsRss().content_rss()
        self.foxsports_media = SportsFeeds.FoxSportsRss().media_rss()
        self.foxsports_link = SportsFeeds.FoxSportsRss().feed_link()



        # THE GUARDIAN WEBSITE FEED.
        # ENTRY 1.
        self.theguardian_title = SportsFeeds.TheGuardienRss().title_rss()
        self.theguardian_content = SportsFeeds.TheGuardienRss().content_rss()
        self.theguardian_media = SportsFeeds.TheGuardienRss().media_rss()
        self.theguardian_link = SportsFeeds.TheGuardienRss().feed_link()



        # BBC SPORTS WEBSITE FEED.
        # ENTRY 1.
        self.bbcsports_title = SportsFeeds.BBCSportRss().title_rss()
        self.bbcsports_content = SportsFeeds.BBCSportRss().content_rss()
        self.bbcsports_media = SportsFeeds.BBCSportRss().media_rss()
        self.bbcsports_link = SportsFeeds.BBCSportRss().feed_link()



        # THE INDEPENDENT WEBSITE FEED.
        # ENTRY 1.
        self.theindependent_title = SportsFeeds.TheIndependentRss().title_rss()
        self.theindependent_content = SportsFeeds.TheIndependentRss().content_rss()
        self.theindependent_media = SportsFeeds.TheIndependentRss().media_rss()
        self.theindependent_link = SportsFeeds.TheIndependentRss().feed_link()



    def DatabaseWriter(self):
        # THE FOX SPORTS DATABASE.
        self.foxsports_feed = FoxSportsDatabase(title_entry=self.foxsports_title,
                                                content_entry=self.foxsports_content,
                                                media_entry=self.foxsports_media,
                                                link_entry=self.foxsports_link)



        self.foxsports_feed.save()



        # THE GUARDIAN DATABASE.
        self.theguardian_feed = TheGuardianDatabase(title_entry=self.theguardian_title,
                                                    content_entry=self.theguardian_content,
                                                    media_entry=self.theguardian_media,
                                                    link_entry=self.theguardian_link)

        self.theguardian_feed.save()



        # BBC SPORTS DATABASE.
        self.bbcsports_feed = BBCSportsDatabase(title_entry=self.bbcsports_title,
                                                content_entry=self.bbcsports_content,
                                                media_entry=self.bbcsports_media,
                                                link_entry=self.bbcsports_link)

        self.bbcsports_feed.save()



        # THE INDEPENDENT DATABASE.
        self.theindependent_feed = TheIndependentDatabase(title_entry=self.theindependent_title,
                                                          content_entry=self.theindependent_content,
                                                          media_entry=self.theindependent_media,
                                                          link_entry=self.theindependent_link)

        self.theindependent_feed.save()



    def Delete_Data(self):
        database_title = FoxSportsDatabase.objects.filter(title_entry=self.foxsports_title)
        database_content = FoxSportsDatabase.objects.filter(content_entry=self.foxsports_content)
        database_media = FoxSportsDatabase.objects.filter(media_entry=self.foxsports_media)
        database_link = FoxSportsDatabase.objects.filter(link_entry=self.foxsports_link)

        database_title.delete()
        database_content.delete()
        database_media.delete()
        database_link.delete()


        theguardian_database_title = TheGuardianDatabase.objects.filter(title_entry=self.theguardian_title)
        theguardian_database_content = TheGuardianDatabase.objects.filter(content_entry=self.theguardian_content)
        theguardian_database_media = TheGuardianDatabase.objects.filter(media_entry=self.theguardian_media)
        theguardian_database_link = TheGuardianDatabase.objects.filter(link_entry=self.theguardian_link)

        theguardian_database_title.delete()
        theguardian_database_content.delete()
        theguardian_database_media.delete()
        theguardian_database_link.delete()


        bbcsports_database_title = BBCSportsDatabase.objects.filter(title_entry=self.bbcsports_title)
        bbcsports_database_content = BBCSportsDatabase.objects.filter(content_entry=self.bbcsports_content)
        bbcsports_database_media = BBCSportsDatabase.objects.filter(media_entry=self.bbcsports_media)
        bbcsports_database_link = BBCSportsDatabase.objects.filter(link_entry=self.bbcsports_link)

        bbcsports_database_title.delete()
        bbcsports_database_content.delete()
        bbcsports_database_media.delete()
        bbcsports_database_link.delete()


        theindependent_database_title = TheIndependentDatabase.objects.filter(title_entry=self.theindependent_title)
        theindependent_database_content = TheIndependentDatabase.objects.filter(content_entry=self.theindependent_content)
        theindependent_database_media = TheIndependentDatabase.objects.filter(media_entry=self.theindependent_media)
        theindependent_database_link = TheIndependentDatabase.objects.filter(link_entry=self.theindependent_link)

        theindependent_database_title.delete()
        theindependent_database_content.delete()
        theindependent_database_media.delete()
        theindependent_database_link.delete()


