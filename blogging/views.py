from django.shortcuts import render  # <- already included there
from django.http import HttpResponse, HttpResponseRedirect, Http404  # added
# add these imports - lesson 07
from django.template import loader
from blogging.models import Post


# Create your views here.
#=========================================================================
#def stub_view(request, *args, **kwargs):
#    body = "Stub View\n\n"
#    if args:
#        body += "Args:\n"
#        body += "\n".join(["\t%s" % a for a in args])
#    if kwargs:
#        body += "Kwargs:\n"
#        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#    return HttpResponse(body, content_type="text/plain")
#=========================================================================

# and add this view
#=========================================================================
#def list_view(request):
#    published = Post.objects.exclude(published_date__exact=None)
#    posts = published.order_by('-published_date')
#    template = loader.get_template('blogging/list.html')
#    context = {'posts': posts}       # We added these next lines just before adding file:
#    body = template.render(context)  # 'list.html' in "blogging/templates/blogging/list.html"
#    return HttpResponse(body, content_type="text/html")  # Finally, build an HttpResponse and return it.
#=========================================================================

#=========================================================================
# Let’s replace most of our view with the render shortcut:
# |--> render(request, template[, ctx][, ctx_instance])

# using: |--> 'from django.shortcuts import render' (which we already had imported), 
# We rewrite our view using above render method:
def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)  # template = loader.get_template('blogging/list.html')

    # This replaces most of our view with the render shortcut.
    # Remember though, all we did manually before is still happening.
#=========================================================================

# Added new view in "Our Detail View" section
def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)  # will add html file next


    #=========================================================================
    # Django templates are rendered by passing in a context.
    # We add our posts to that context so they can be used by the template.

    # Then, we build an HttpResponse and return it. This is, fundamentally,
    # no different from the stub_view just before.
 
    # --> We still need to fix the url for our blog index page.
    #=========================================================================