from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "POST":
        items = request.POST.get("fullValues","")
        print("\n")
        item_list = decode_item_request(items)
        handle_item_request(item_list)

    return render(request,"foodsrch/index.html")



def handle_item_request(items):
    print("Post Handling")
    

"A function that is used by handle_item to decrypt the original item request"
def decode_item_request(item_request):
    all_items = item_request.split("-")
    all_items.remove("")
    return all_items