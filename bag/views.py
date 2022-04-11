from django.shortcuts import redirect, render

from django.shortcuts import render


def view_bag(request):
    """View to return the shopping bag contents page"""

    template = "bag/bag.html"
    return render(request, template)


def add_to_bag(request, item_id):
    """Add a new item to the shopping bag"""

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session["bag"] = bag
    print(request.session["bag"])
    return redirect(redirect_url)