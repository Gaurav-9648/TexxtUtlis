# self

from django.http import HttpResponse
from django.shortcuts import render
# def hacker_rank(request):
#     return HttpResponse('''<a href = "https://www.hackerrank.com/dashboard">Hacker Rank</a>''')
#
# def code_chef(request):
#     return HttpResponse('''<a href = "https://www.codechef.com/">Code Chef</a>''')
#
# def Youtube(request):
#     return HttpResponse('''<a href = "https://www.youtube.com">Youtube</a>''')
#
# def GL(request):
#     return HttpResponse('''<a href = "https://www.mygreatlearning.com/academy">Great Learning</a>''')
#
# def udemy(request):
#     return HttpResponse('''<a href = "https://www.udemy.com">Udemy</a>''')


# 7 video

def index(request):
    return render(request,"index.html")

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
