from django.contrib import admin
from tracker.models import * 
# Register your models here.

#To modify django admin name which is present by default
admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"

admin.site.register(CurrentBalance)


#At present this is present in lines we can modify this to tables 
class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "amount",
        "current_balance",
        "expense_type",
        "description",
        "created_at",
    ]

    search_fields = ['expense_type']
    ordering = ['-created_at']
    Filter = ['expense_type']
#below by adding trackinghistoryadmin in this way to see tables
admin.site.register(TrackingHistory ,TrackingHistoryAdmin)
