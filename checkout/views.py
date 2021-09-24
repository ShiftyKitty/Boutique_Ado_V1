from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JdIFMCgA9z4ehGFIyTn1oZcs37BznsXFZWsO40mEuSIqpnFIEDtekXyFS6iKe6D6GUhrhsnH9pA6y0IZruZ2jul00rOSUQ54w',
    }

    return render(request, template, context)