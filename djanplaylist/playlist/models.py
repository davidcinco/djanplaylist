from django.db import models

# Create your models here.

class Artist(models.Model):
    artistid = models.AutoField(primary_key=True)
    artistname = models.CharField(max_length=195)

    class Meta:
        managed = False
        db_table = 'artist'

class Album(models.Model):
    albumid = models.AutoField(primary_key=True)
    albumname = models.CharField(max_length=185)
    albumgenre = models.CharField(max_length=185)
    artistfrom = models.ForeignKey('Artist', models.DO_NOTHING, db_column='artistfrom', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'

class Song(models.Model):
    songid = models.AutoField(primary_key=True)
    songname = models.TextField()
    albumfrom = models.ForeignKey(Album, models.DO_NOTHING, db_column='albumfrom')

    class Meta:
        managed = False
        db_table = 'song'

