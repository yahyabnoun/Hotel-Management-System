
from django.contrib import admin 
from hotel.models import Hotel ,Booking, ActivityLog, HotelGallery, StaffOnDuty, Room, RoomType



class HotelGalleryInline (admin. TabularInline): 
    model = HotelGallery

class HotelAdmin(admin. ModelAdmin):
    inlines = [HotelGalleryInline] 
    list_display= ['thumbnail', 'name', 'user', 'status'] 
    prepopulated_fields = {"slug": ("name", )}
    
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)
admin.site.register(ActivityLog)
admin.site.register(StaffOnDuty)
admin.site.register(Room)
@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'type', 'price', 'number_of_beds', 'room_capacity', 'slug', 'date')
    search_fields = ('hotel__name', 'type')
    prepopulated_fields = {'slug': ('type',)} 

 