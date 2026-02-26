from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):

    if request.method != "POST":
        return HttpResponse("Invalid request method")

    text = request.POST.get('text', '').strip()

    if not text:
        return HttpResponse("Please enter some text")

    remove_punc = request.POST.get('removepunc')
    fullcaps = request.POST.get('fullcaps')
    newlineremover = request.POST.get('newlineremover')
    extraspaceremover = request.POST.get('extraspaceremover')

    analyzed = text
    operations = []

    # 1️⃣ Remove punctuation
    if remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''.join(char for char in analyzed if char not in punctuations)
        operations.append("Removed Punctuation")

    # 2️⃣ Uppercase
    if fullcaps == "on":
        analyzed = analyzed.upper()
        operations.append("Converted to Uppercase")

    # 3️⃣ Remove new lines
    if newlineremover == "on":
        analyzed = analyzed.replace("\n", "").replace("\r", "")
        operations.append("Removed New Lines")

    # 4️⃣ Remove extra spaces
    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())
        operations.append("Removed Extra Spaces")

    if not operations:
        return HttpResponse("Please select at least one operation")

    context = {
        "purpose": ", ".join(operations),
        "analyzed_text": analyzed
    }

    return render(request, 'analyze.html', context)