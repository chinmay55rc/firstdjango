from django.contrib import admin
from home.models import Book,Author,Genre

# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=['id','name']
    fields=(('name','purchase_date'),('genre','book_author'))
    list_filter=('name','purchase_date',('Author',admin.RelatedOnlyFieldListFilter))
    list_filter=['name','purchase_date','book_author']
   # pass

@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class BookAdmin(admin.ModelAdmin):
    pass



