from django.shortcuts import render_to_response, get_object_or_404
from django.utils.simplejson import dumps as json_encode
from django.http import HttpResponse

from time import mktime

import MySQLdb


def _db():
    return MySQLdb.connect(
            user="twit02",
            passwd="frayedwell",
            db="twit02",
            host="hamm.cs.tamu.edu" )


def _db_cur():
    return _db().cursor(MySQLdb.cursors.DictCursor)


def twtop_t(request):
    top_t = ('toyo_hasa','tac0','twhive_w20','tommytrc','traciknoppe','techfrog','twishes','tomoyuji','tom','tato256','terrywhalin','teifion','tetra11','teenbizcoach','tatsu','terrizsoloceo','takowasabi','taitoku','thehodge','tjakkahhh','thescicoach','tjonsek','tgn','thomasclifford','twhillary','tsx','techbabe','timanrebel','trucklover','twishes_de','theclimbergirl','tuya28','taylorbanks','tomo154','tiagotex','thiago_p','thechrisd','tentekomind','tomcapote','toddkane')
    return render_to_response('proj/twtopletter.html', {'toptw':top_t[:2]})


def twtop3(request, name):
    return render_to_response('proj/twtopletter.html', {'toptw':(name,)})


def twtop(request):
    # get top 30 users for the time period

    top30 = [
    # ('expensiveguy',135293),
    ('jonasbrothers',7013), ('donniewahlberg',4000),
    # ('getmoretweeple',777538),
    ('ivetesangalo',48520), ('federicodevito',33434), ('justinbieber',18285), ('addthis',3056), ('selenagomez',4090), ('taylorswift13',3044), ('jonathanrknight',5222), ('ddlovato',3801), ('krisallen4real',31149), ('mileycyrus',4246), ('eduardosurita',35037), ('tweetmeme',3279), ('mashable',7122), ('officialtila',14499), ('souljaboytellem',4307), ('tommcfly',6960), ('pink',9361), ('coelhors',50514), ('revrunwisdom',6743), ('ogochocinco',22922), ('cesarganso',665551), ('jordanknight',11788), ('christianpior',19063), ('songzyuuup',3667), ('caiquenogueira',23459), ('lilduval',24281), ('iamdiddy',2813), ('adamlambert',26952), ('danilogentili',8134), ('myfabolouslife',11426), ('davidarchie',9242)]

    return render_to_response('proj/twtop.html', {'toptw': top30[:12]})


def twchart(request, num):
    c = _db_cur()
    num = int(num)
    x= c.execute("select screen_name from twitter_twitaccount where id = %s",(num,))
    if x:
        name = c.fetchone()['screen_name']
        return render_to_response('proj/twchart.html', {'name': name, 'twnum':num})
    else:
        return HttpResponse("no")


def twdata(request, num):
    num = int(num)
    c = _db_cur()
    c.execute("""
select to_user_id, as_of_time, score 
from user_ranking 
where to_user_id = %s and as_of_time >= '2009-09-15'
        """,(num,))
    data = [(1000 * mktime(d['as_of_time'].timetuple()), d['score']) for d in c]
    return HttpResponse( "d_%d = %s;" % (num, json_encode(data))) 


def twletterdata(request, name):
    c = _db_cur()
    c.execute("""
select as_of,sum(score03) as score03, sum(score10) as score10, sum(score50) as  score50
from """ + "scores_%s"%name.lower()[0] + """
where to_user = %s group by as_of """,(name.lower(),))
    data = {'d03':[], 'd10':[], 'd50':[]}
    for d in c:
        data['d03'].append((1000 * mktime(d['as_of'].timetuple()), d['score03']))
        data['d10'].append((1000 * mktime(d['as_of'].timetuple()), d['score10']))
        data['d50'].append((1000 * mktime(d['as_of'].timetuple()), d['score50']))
    return HttpResponse( "d_%s = %s;" % (name, json_encode(data))) 


