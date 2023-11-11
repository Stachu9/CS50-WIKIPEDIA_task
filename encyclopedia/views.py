from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from . import util
import markdown
from django.contrib import messages
import random

class NewEntryForm(forms.Form):
    title = forms.CharField(label="New entry title")
    text = forms.CharField(label="New entry text")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() })

def entryPage(request, entry=""):
    if entry in util.list_entries():
        html = {
            'html': markdown.markdown(util.get_entry(entry)),
            "entry": entry
        }
        return render(request, "encyclopedia/entry-page.html", html)
    else:
        return HttpResponse("Entry does not exist")

def searchBox(request):
    if request.method == "POST":
        search = request.POST["q"]
        resultList = []
        for element in util.list_entries():
            if element.lower() == search.lower():
                return redirect("/{}" .format(element))
            if search.lower() in element.lower():
                resultList.append(element)
        if len(resultList) == 0:
            return HttpResponse("No results")
        else:
            return render(request, "encyclopedia/result-page.html", {"results": resultList})
    else:
        return redirect("/")
    
def newPage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
        else:
            return render(request, "encyclopedia/new-page.html", {"form": NewEntryForm()})
        if title in util.list_entries():
            return HttpResponse("Entry already exist")
        else:
            util.save_entry(title, text)
            return redirect("/{}" .format(title))
    else:
        return render(request, "encyclopedia/new-page.html", {"form": NewEntryForm()})
        
def editPage(request):
    if "redirect" in request.POST:
        entry = request.POST["entry"]
        text = util.get_entry(entry)
        return render(request, "encyclopedia/edit-page.html", {"text":text, "entry":entry})
    if "editText" in request.POST:
        newText = request.POST['newText']
        title = request.POST['title']
        util.save_entry(title, newText)
        return redirect("/{}" .format(title))
    else:
        return redirect("/")
    
def randomPage(request):
    randomEntry = random.choice(util.list_entries())
    return redirect("/{}" .format(randomEntry))





