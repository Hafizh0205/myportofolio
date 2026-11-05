from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, QueryDict
from django.views.decorators.http import require_http_methods
from .models import Contact

# 1. Menampilkan Halaman Utama
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts_index.html", {"contacts": contacts})

# 2. Menambah Kontak (POST)
def contact_add(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
        )
    contacts = Contact.objects.all()
    return render(request, "_contact_rows.html", {"contacts": contacts})

# 3. Menghapus Kontak (DELETE)
@require_http_methods(["DELETE"])
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponse("")

# 4. Pencarian Langsung Live Search (GET)
def contact_search(request):
    query = request.GET.get("q", "")
    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, "_contact_rows.html", {"contacts": contacts})

# 5. Mengambil Row Edit (GET)
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "_contact_edit_row.html", {"contact": contact})

# 6. Mengambil Row Normal / Batal (GET)
def contact_row(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "_contact_row.html", {"contact": contact})

# 7. Menyimpan Hasil Update (PUT)
@require_http_methods(["PUT"])
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    data = QueryDict(request.body)
    contact.name = data.get("name", contact.name)
    contact.email = data.get("email", contact.email)
    contact.save()
    return render(request, "_contact_row.html", {"contact": contact})