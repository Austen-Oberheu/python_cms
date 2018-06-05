from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
 
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .models import Page, PageContent

mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
 
 
def mobileBrowser(request):
    # Super simple device detection, returns True for mobile devices
 
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser
 
 
def PageView(request, page_id, page_url=Page.page_url):

    page = get_object_or_404(Page, pk=page_id)
    content = get_object_or_404(PageContent, pk=page_id)
 
    if mobileBrowser(request):
        template = loader.get_template('pages/m_index.html')
    else:
        template = loader.get_template('pages/index.html')
 
    return HttpResponse(template.render({'page': page,'content': content}))


# def PageView(request, page_id, page_url=Page.page_url):
#     page = get_object_or_404(Page, pk=page_id)
#     content = get_object_or_404(PageContent, pk=page_id)
#     return render(request, 'pages/home.html', {'page': page,
#                                                 'content': content})
