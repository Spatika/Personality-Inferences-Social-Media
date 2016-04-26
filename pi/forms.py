from django import forms

from .models import InputFeature

class InputFeatureForm(forms.ModelForm):

    class Meta:
        model = InputFeature

        fields = ('name', 'Analytic', 'Clout', 'Authentic', 'Tone', 'self_refs', 'social_words', 'pos_emo',
        'neg_emo', 'cog_words', 'art_words', 'big_words', 'Age', 'Friends',
        'Groups', 'fb_degree', 'Likes','Events', 'photos_uploaded',
        'photos_tagged_in', 'a_score', 'c_score', 'e_score', 'es_score',
        'o_score',)

        labels = { 'name': 'Name',
            'Analytic' : 'LIWC Analytic Score',
            'Clout' : 'LIWC Clout Score',
            'Authentic' : 'LIWC Authentic Score',
            'Tone' : 'LIWC Tone Score',
            'self_refs': 'LIWC Self Reference Words',
            'social_words': 'LIWC Social Words',
            'pos_emo' : 'Positive Emotion Words',
            'neg_emo' : 'Negative Emotion Words',
            'cog_words' : 'Cognitive Words',
            'art_words' : 'Article Words',
            'big_words' : 'Big Words (>6 Letters)',
            'fb_degree' : 'Facebook Degree of Separation',
            'photos_tagged_in' : 'Number of Photos Tagged in',
            'photos_uploaded' : 'Number of Photos Uploaded',
            'a_score' : 'Agreeableness Score from Survey',
            'c_score' : 'Conscientiousness Score from Survey',
            'e_score' : 'Extraversion Score from Survey',
            'es_score' : 'Emotional Stability Score from Survey',
            'o_score' : 'Openness Score from Survey'
         }
