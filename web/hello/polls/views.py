from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice,mapmat
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
import datetime
import MySQLdb



# Create your views here.

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'


class RenderMap(generic.DetailView):
    model=mapmat
    template_name='polls/rendermap.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def Qrendermap(request):
    db=MySQLdb.connect("127.0.0.1","root","198123","mapdb")
    cursor=db.cursor()
    sql="SELECT * FROM mapdb.polls_mapmat"
    mapData={}
    #context=RequestContext(request, {'mapData':mapData,})
    context=None
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:            
            mapData['address']=row[1]
            #mapData[row[1]]['lng']=row[2]
            #mapData[row[1]]['lat']=row[3]
            #now = datetime.datetime.now()
            #html = "<html><body>It is now %s,%s,%s,%s.</body></html>" % (address,lng,lat,now)
            print mapData
        print type(mapData)
        context=RequestContext(request, {'mapData':mapData,})
    except:
         print "Error: unable to fecth data"
    db.close()
    return render(request,'polls/rendermap.html',context)