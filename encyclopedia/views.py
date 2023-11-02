from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

from . import util

import markdown


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
        
                
