from django.shortcuts import render
from .models import BookModel, PageModel, ImageModel

# Create your views here.
def book_name(request):
    books = BookModel.objects.all()
    return render(request, 'book.html',{'books':books})


def book_page(request, book_id, page_num):
    context = {}
    page_obj = PageModel.objects.get(b_id = book_id , page_no = page_num)
    context["page"] = page_obj
    
    book_obj = BookModel.objects.get(id = book_id)
    context["book"] = book_obj
 
    prev_page = page_num - 1
    prev_page_obj = PageModel.objects.filter(b_id=book_id, page_no=prev_page).first()
    context["prev"] = prev_page_obj

    next_page = page_num + 1
    next_page_obj = PageModel.objects.filter(b_id=book_id, page_no=next_page).first()
    context["next"] = next_page_obj 

    img_obj = ImageModel.objects.all()
    context["img"] = img_obj

    return render(request, 'page.html', context)
