from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



"""
    for adding the customizble options
"""

def options(request, optionid):

    match optionid:
        case "text_val":
            context = {"text": "text"}   
        case "textarea_val":
            context = {"textarea": "textarea"}   
        case "checkbox_val":
            context = {"checkbox": "checkbox"}   
        case "radio_val":
            context = {"radio": "radio"}   
        case "select_val":
            context = {"select": "select"}   
         

    return render(request, "options.html", context )


@csrf_exempt
def add_sub_options(request, id):

    match id:
        case "checkbox_options":
            context = {"checkbox_options": "checkbox_options"}   
        case "radio_options":
            context = {"radio_options": "radio_options"}  
    
    return render(request, "options.html", context )


@csrf_exempt
def delete_sub_options(request):
    return render(request, "options.html")

