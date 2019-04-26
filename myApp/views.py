from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required
def Home(request):
    return render(request, 'myApp/home.html')


def Analyze(request):
    input_text = request.POST.get('text')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    count = request.POST.get('count', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    analyzed_text = ""

    if input_text == '':
        return redirect('home')

    if removepunc == 'on':
        punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        for char in input_text:
            if char not in punctuations:
                analyzed_text = analyzed_text + char
        
        context = {
            'task':'Remove Punctuations',
            'analyzed_text':analyzed_text
        }

        input_text = analyzed_text
        #return render(request, 'myApp/result.html', context)
    
    if fullcaps == "on":
        analyzed_text = input_text.upper()
        context = {
            'task':'Capitalize Letters',
            'analyzed_text':analyzed_text
        }

        input_text = analyzed_text
        #return render(request, 'myApp/result.html', context)
        
        #return render(request, 'myApp/result.html', context)

    if newlineremover == 'on':
        analyzed_text = ''
        for char in input_text:
            if char != '\n' and char != '\r':
                analyzed_text = analyzed_text + char
        
        context = {
            'task':'New Line Remover',
            'analyzed_text':analyzed_text
        }

        input_text = analyzed_text
        #return render(request, 'myApp/result.html', context)
    
    if spaceremover == 'on':
        analyzed_text = " ".join(input_text.split())
        context = {
            'task':'Extra Space Remover',
            'analyzed_text':analyzed_text
        }

        input_text = analyzed_text
    
    if count == 'on':
        words = input_text.split()
        total_words =  str(len(words))
        context = {
            'task':'Count Words',
            'count': 'Total words:' + total_words,
        }
        input_text = analyzed_text

    return render(request, 'myApp/result.html', context)

        

    

