from __future__ import unicode_literals

from django.db import models

# Create your models here.

class InputFeature(models.Model):
    name = models.CharField(max_length=200, default="Your Name Here")
    Analytic = models.FloatField(default = 0.0)
    Clout = models.FloatField(default=0.0)
    Authentic = models.FloatField(default=0.0)
    Tone = models.FloatField(default=0.0)
    self_refs = models.FloatField(default=0.0)
    social_words = models.FloatField(default=0.0)
    pos_emo = models.FloatField(default=0.0)
    neg_emo = models.FloatField(default=0.0)
    cog_words = models.FloatField(default=0.0)
    art_words = models.FloatField(default=0.0)
    big_words = models.FloatField(default=0.0)
    Age = models.IntegerField(default=0)
    Friends = models.IntegerField(default=0)
    Groups = models.IntegerField(default=0)
    fb_degree = models.FloatField(default=0.0)
    Likes  = models.IntegerField(default=0)
    Events = models.IntegerField(default=0)
    photos_uploaded = models.IntegerField(default=0)
    photos_tagged_in = models.IntegerField(default=0)
    a_score = models.IntegerField(default=0)
    c_score = models.IntegerField(default=0)
    e_score = models.IntegerField(default=0)
    es_score = models.IntegerField(default=0)
    o_score = models.IntegerField(default=0)
    already_evaluated = models.BooleanField(default=False)

    def __str__(self):
        return self.name



#right now, just for Extraversion
class OutputFeature(models.Model):
    input_features = models.ForeignKey(InputFeature)
    e_actual_label = models.FloatField(default=0.0)
    e_scored_label = models.FloatField(default=0.0)

    a_actual_label = models.FloatField(default=0.0)
    a_scored_label = models.FloatField(default=0.0)

    c_actual_label = models.FloatField(default=0.0)
    c_scored_label = models.FloatField(default=0.0)

    es_actual_label = models.FloatField(default=0.0)
    es_scored_label = models.FloatField(default=0.0)

    o_actual_label = models.FloatField(default=0.0)
    o_scored_label = models.FloatField(default=0.0)



    @classmethod
    def create(cls, input_features, e_actual_label, e_scored_label, a_actual_label, a_scored_label, c_actual_label, c_scored_label, es_actual_label, es_scored_label, o_actual_label, o_scored_label):
        outputfeature = cls(input_features = input_features, e_actual_label = e_actual_label, e_scored_label = e_scored_label,
        a_actual_label = a_actual_label, a_scored_label = a_scored_label, c_actual_label = c_actual_label, c_scored_label = c_scored_label, es_actual_label = es_actual_label,
        o_actual_label = o_actual_label, o_scored_label=o_scored_label, es_scored_label=es_scored_label)
        # do something with the book
        return outputfeature


#class MLModel(models.Model):
#    target = models.CharField(max_length=200) #can be E, ES, A, O or C
#    api_key = models.CharField(max_leght=1000)
