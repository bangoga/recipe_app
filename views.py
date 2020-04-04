from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import os
# Create your views here.

def index(request):
    if request.method == "POST":
        items = request.POST.get("fullValues","")
        print("\n")
        # item_list = decode_item_request(items)
        # handle_item_request(item_list)
        return render(request,"foodsrch/search_result_list.html",{'item':item_list})

    else:
        spiceList = readTxt()
        return render(request,"foodsrch/index.html",{'spices':spiceList})



#----------------------------------- [Reads all the possible spices from the local txt file]-------------------------------#
def readTxt():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'spice.txt')   # Reads line by line and saves them to data[]
    with open(file_path , 'r') as f:
        data = [line.strip() for line in f]
    print(data[1])

    return data














def handle_item_request(items):
    print(items)
    print("Post Handling")


"A function that is used by handle_item to decrypt the original item request"
def decode_item_request(item_request):
    all_items = item_request.split("-")
    all_items.remove("")
    return all_items

def result(request):
    return render(request,"foodsrch/search_result_list.html",{'post':'Why is this working or is it really working? '})

"Current its being shown as such but what if you what is class rendering?"
