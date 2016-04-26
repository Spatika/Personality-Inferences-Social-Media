from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.core import serializers
from django.template import loader
from .forms import InputFeatureForm
from django.shortcuts import redirect

from .models import InputFeature
from .models import OutputFeature

from django.utils.encoding import force_text

import urllib2
import json


def instancelist(request):
    inputs = InputFeature.objects.all()
    context = {
        'inputs': inputs,
    }
    return render(request, 'pi/instancelist.html', context)


#inputfeature_edit.html
def inputfeature_new(request):
    if request.method == "POST":
        form = InputFeatureForm(request.POST)
        if form.is_valid():
            new_instance = form.save(commit=False)
            #form.fields['Cog words'] =
            #instance.author = request.user
            #post.published_date = timezone.now()
            new_instance.save()

            #redirect to results view to run the ML model on the input
            return redirect('results', new_instance.pk)
    else:
        form = InputFeatureForm()

    return render(request, 'pi/inputfeature_edit.html', {'form': form})

##Index.html
def index(request):

    latest_input_list = InputFeature.objects.all()
    template = loader.get_template('pi/index.html')
    context = {
        'latest_input_list': latest_input_list,
    }
    return render(request, 'pi/index.html', context)

##About.html
##Index.html
def about(request):

    template = loader.get_template('pi/about.html')

    return render(request, 'pi/about.html')


##Instance.html
def instance(request, instance_id):

    try:
        instance = InputFeature.objects.get(pk=instance_id)
    except InputFeature.DoesNotExist:
        raise Http404("Instance does not exist")
    return render(request, 'pi/instance.html', {'instance' : instance})

##Results.html
def results(request, instance_id):
    try:
        instance = InputFeature.objects.get(pk=instance_id)

        if(InputFeature.objects.get(pk=instance_id).already_evaluated == True):
                #redirect to results view to run the ML model on the input
                return redirect('results', instance_id)

        #[(getattr(instance,field.name)) for field in instance._meta.fields]
        #serialized_object = serializers.serialize("json", [instance,])

        #print(serialized_object.pk)


        instance_self_refs = str(InputFeature.objects.get(pk=instance_id).self_refs)
        instance_social_words = str(InputFeature.objects.get(pk=instance_id).social_words)
        instance_analytic  = InputFeature.objects.get(pk=instance_id).Analytic
        instance_clout = InputFeature.objects.get(pk=instance_id).Clout
        instance_authentic = InputFeature.objects.get(pk=instance_id).Authentic
        instance_tone = InputFeature.objects.get(pk=instance_id).Tone
        instance_pos_emo =  InputFeature.objects.get(pk=instance_id).pos_emo
        instance_neg_emo =  InputFeature.objects.get(pk=instance_id).neg_emo
        instance_cog_words = InputFeature.objects.get(pk=instance_id).cog_words
        instance_art_words = InputFeature.objects.get(pk=instance_id).art_words
        instance_big_words = InputFeature.objects.get(pk=instance_id).big_words
        instance_age = InputFeature.objects.get(pk=instance_id).Age
        instance_friends = InputFeature.objects.get(pk=instance_id).Friends
        instance_groups = InputFeature.objects.get(pk=instance_id).Groups
        instance_fb_degree = InputFeature.objects.get(pk=instance_id).fb_degree
        instance_likes = InputFeature.objects.get(pk=instance_id).Likes
        instance_events =InputFeature.objects.get(pk=instance_id).Events
        instance_photosuploaded = InputFeature.objects.get(pk=instance_id).photos_uploaded
        instance_photostagged = InputFeature.objects.get(pk=instance_id).photos_tagged_in
        instance_ascore = InputFeature.objects.get(pk=instance_id).a_score
        instance_cscore = InputFeature.objects.get(pk=instance_id).c_score
        instance_escore = InputFeature.objects.get(pk=instance_id).e_score
        instance_oscore =  InputFeature.objects.get(pk=instance_id).o_score
        instance_es_score =  InputFeature.objects.get(pk=instance_id).es_score


        print(instance_self_refs)


        data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": [  "Analytic", "Clout", "Authentic", "Tone",
                    "LIWC - Self-References", "LIWC - Social Words", "LIWC - Positive Emotions", "LIWC - Negative Emotions",
                    "Overall Cognitive Words", "Articles (a, an, the)", "\"\"Big\"\" Words (> 6 letters)",
                    "Age", "Friends", "Groups", "FB Degree of Separation",
                    "Likes", "Events", "Photos Uploaded", "Photos Tagged In",  "E Score", "A Score", "C Score", "ES Score", "O Score"],
                    "Values": [ [ instance_analytic, instance_clout, instance_authentic, instance_tone, instance_self_refs, instance_social_words, instance_pos_emo, instance_neg_emo, instance_cog_words, instance_art_words, instance_big_words, instance_age, instance_friends, instance_groups, instance_fb_degree,
                    instance_likes, instance_events, instance_photosuploaded, instance_photostagged,  instance_escore , instance_ascore, instance_cscore, instance_es_score, instance_oscore], ]
                },        },
            "GlobalParameters": {
}
    }

        body = str.encode(json.dumps(data))

        #######EXTRAVERSION######
        url = 'https://ussouthcentral.services.azureml.net/workspaces/14ff36794f6e438e9748d5f277a94111/services/6b689b88e08d4d02a7477345e6d8f736/execute?api-version=2.0&details=true'
        api_key = 'nsMT18VID9Pw+daL7K4HkaDfphSgCTWkmQtLa5tu91Noc3SjxTbW9J0RDZY+ORUQkHPDOeiPkwzSkDg1QgvYaw==' # Replace this with the API key for the web service

        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'Accept':'application/json'} #Indicate that you are accepting response ALSO in JSON format

        req = urllib2.Request(url, body, headers)

        try:
            response = urllib2.urlopen(req)
            print("entering second try block")
            #block till url result is ready
            result = json.loads(response.read())

            #create new OutputFeature only NOT save it to the database

            e_actual_label = result['Results']['output1']['value']['Values'][0][0]
            e_scored_label = result['Results']['output1']['value']['Values'][0][1]



        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))
        ######END EXTRAVERSION########

        #######AGREEABLENESS######
        url = 'https://ussouthcentral.services.azureml.net/workspaces/14ff36794f6e438e9748d5f277a94111/services/953b4e5445c141ad9e28c975e818342c/execute?api-version=2.0&details=true'
        api_key = 'vCVCxc+CAd8H/2h6i2tHMFUmuCeaotQ1GgLHeDdTkZNUMW3pA1Pr2xiDcPtALaie4vnpHBdIz5CjMTImbCy/Wg==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'Accept':'application/json'} #Indicate that you are accepting response ALSO in JSON format

        req = urllib2.Request(url, body, headers)

        try:
            response = urllib2.urlopen(req)
            print("entering second try block")
            #block till url result is ready
            result = json.loads(response.read())

            #create new OutputFeature only NOT save it to the database

            a_actual_label = result['Results']['output1']['value']['Values'][0][0]
            a_scored_label = result['Results']['output1']['value']['Values'][0][1]



        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))
        ######END AGREEABLESS########

        #######OPENNESS######
        url = 'https://ussouthcentral.services.azureml.net/workspaces/14ff36794f6e438e9748d5f277a94111/services/9b60b582d95d4da3a59a3ffa633d6b14/execute?api-version=2.0&details=true'
        api_key = 'xkSmpN3wI2odEgwQiUBs+aMKqRkfNmeNny3TXJD0U4ku0vIBHLgZvWPjksibVnO5EWm5kMYc2CG9ZMv2yAvnyQ==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'Accept':'application/json'} #Indicate that you are accepting response ALSO in JSON format

        req = urllib2.Request(url, body, headers)

        try:
            response = urllib2.urlopen(req)
            print("entering second try block")
            #block till url result is ready
            result = json.loads(response.read())

            #create new OutputFeature only NOT save it to the database

            o_actual_label = result['Results']['output1']['value']['Values'][0][0]
            o_scored_label = result['Results']['output1']['value']['Values'][0][1]



        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))
        ######END OPENNESS########

        #######CONSCIENTIOUSNESS######
        url = 'https://ussouthcentral.services.azureml.net/workspaces/14ff36794f6e438e9748d5f277a94111/services/2a112206f51c4ca0beafbff70fd0ce5e/execute?api-version=2.0&details=true'
        api_key = 'kKPl8Qc6nt+VZgrBgf4sTulVEai07TJP6pY3KrVBs2HB2CUB0UrBrh8ettbyqoeuYIGaqBgK2c357KqFmkJRIg==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'Accept':'application/json'} #Indicate that you are accepting response ALSO in JSON format

        req = urllib2.Request(url, body, headers)

        try:
            response = urllib2.urlopen(req)
            print("entering second try block")
            #block till url result is ready
            result = json.loads(response.read())

            #create new OutputFeature only NOT save it to the database

            c_actual_label = result['Results']['output1']['value']['Values'][0][0]
            c_scored_label = result['Results']['output1']['value']['Values'][0][1]



        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))
        ######END CONSCIENTIOUSNESS########

        #######Emotional Stability######
        url = 'https://ussouthcentral.services.azureml.net/workspaces/14ff36794f6e438e9748d5f277a94111/services/56aa9c91941f4f8386ee5d788d6cb71c/execute?api-version=2.0&details=true'
        api_key = 'tYPe2iPMPRMkhZjdU+2IE5o5T/0/cD6yrUbVkVEMP3RgaqIvObEVQhRMlRxL04f8XVx1ZVYws1Dax/3+uaERyw==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'Accept':'application/json'} #Indicate that you are accepting response ALSO in JSON format

        req = urllib2.Request(url, body, headers)

        try:
            response = urllib2.urlopen(req)
            print("entering second try block")
            #block till url result is ready
            result = json.loads(response.read())

            #create new OutputFeature only NOT save it to the database

            es_actual_label = result['Results']['output1']['value']['Values'][0][0]
            es_scored_label = result['Results']['output1']['value']['Values'][0][1]



        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))
        ######END Emotional Stability########

        output_object = OutputFeature.create(instance, e_actual_label, e_scored_label, a_actual_label, a_scored_label, c_actual_label, c_scored_label, es_actual_label, es_scored_label, o_actual_label, o_scored_label)

        #save to DB, after accumulated all 10 labels
        output_object.save()
        instance.already_evaluated = True

    except InputFeature.DoesNotExist:
        raise Http404("Instance does not exist")
    return render(request, 'pi/results.html', {'output' : output_object})


def runmodel(request, instance_id):
    return HttpResponse("You're trying to run personality insights for instance %s." % instance_id)
