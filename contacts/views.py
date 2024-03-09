from django.shortcuts import render
from django.forms import formset_factory
from .forms import ContactForm

ContactFormSet = formset_factory(ContactForm, extra=2)

def contact_view(request):
    if request.method == 'POST':
        formset = ContactFormSet(request.POST)
        if formset.is_valid():
            # Process the forms
            pass
    else:
        formset = ContactFormSet()
    context = {
        'formset': formset
    }
    return render(request, 'contact.html', context)
