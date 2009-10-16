from django.shortcuts import render_to_response, get_object_or_404
from django.utils.simplejson import dumps as json_encode
from django.http import HttpResponse

from datetime import datetime, timedelta
from time import mktime

from stats.models import StatKey, StatPoint, StatFlag

def chart(request, key):
    skey = StatKey.objects.get(term=key[:16])
    if not skey: return HttpResponse("no")
    return render_to_response('stats/chart.html', {'statkey': skey.term})


def _flag_status(myFlag):
    # take care of the easy cases
    if myFlag.flag_value == 0: return "fin"
    if myFlag.flag_value < 0: return "err"

    # check if the job has stalled
    expiretime = myFlag.last_updated + timedelta(minutes=myFlag.expires)
    if datetime.now() > expiretime: return "stall"

    if myFlag.flag_value > 1: return "run"
    else: return "start" # myFlag.flag_value == 1:


def flag(request, name):
    myFlag = StatFlag.objects.get(flag_name=name[:16])
    if not myFlag: return HttpResponse("no")
    myFlag.status = _flag_status(myFlag)
    return render_to_response('stats/flag.html', {
        'flag': myFlag,
        })


def index(request):
    flags = StatFlag.objects.order_by('-last_updated')[:10]
    for f in flags:
        f.status = _flag_status(f)
    statkeys = [s.term for s in StatKey.objects.order_by('-last_update')[:3]]
    return render_to_response(
        'stats/index.html', 
        {'flags': flags, 'statkeys':statkeys},
        )


def new(request, key, point):
    if len(key) > 16: 
        return HttpResponse("StatKey must be no longer than 16 characters.")
    skey,_created = StatKey.objects.get_or_create(term=key[:16])
    if _created:
        skey.descr = ""
    skey.save()
    try:
        point = float(point)
    except:
        return HttpResponse("StatPoint conversion failure.  Must be float.")
    spt = StatPoint(statkey=skey, value=point)
    spt.save()
    return HttpResponse("ok %s %6.6f" % (key, point))


def newflag(request, name, value, stat_text=None):
    if len(name) > 16: 
        return HttpResponse("FlagName must be no longer than 16 characters.")
    flag,_created = StatFlag.objects.get_or_create(flag_name=name[:16])
    try:
        value = int(value)
    except:
        return HttpResponse("Value conversion failure.  Must be int.")
    flag.flag_value = value
    flag.stat_text = stat_text
    flag.save()
    return HttpResponse("ok %s %d" % (name, value))


def stat_data(request, key):
    skey = StatKey.objects.get(term=key[:16])
    if not skey: return HttpResponse("no")
    data = StatPoint.objects.filter(statkey=skey).order_by('-created_at')[:1000]
    return HttpResponse(key + " = " + json_encode( [
        (1000*mktime(d.created_at.timetuple()), d.value) for d in data
        ] ) + ";" )


