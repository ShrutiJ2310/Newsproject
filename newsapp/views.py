from django.shortcuts import render, redirect
from requests import *

def pnf(request, exception):
	return redirect("home")

def home(request):
	try:
		a1 = "https://newsapi.org/v2/top-headlines"
		a2 = "?country=in"
		a3 = "&apiKey=a60fa897c0ce4f4b9a35783f68a8a7b5"
		wa = a1 + a2 + a3
		res = get(wa)
		data = res.json()
		info = data["articles"]
		msg = info
		return render(request,"home.html",{"msg":msg})
	except Exception as e:
		return render(request,"home.html",{"msg":str(e)})
	
def about(request):
	return render(request,"about.html")
