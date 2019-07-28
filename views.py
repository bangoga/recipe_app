from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "POST":
        items = request.POST.get("fullValues","")
        print("\n\n")
        print(items)
        
    return render(request,"foodsrch/index.html")



def handle_item_request(items):
    print("handling")


"A function that is used by handle_item to decrypt the original item request"
def decode_item_request(item_request):
    print("decoding")