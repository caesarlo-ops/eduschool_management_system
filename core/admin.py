from django.contrib import admin
from .models import Student, Employee, Fee, Attendance, UserProfile, Receipt, ReceiptItem


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_class', 'parent_name', 'contact', 'created_at']
    list_filter = ['student_class', 'created_at']
    search_fields = ['name', 'parent_name', 'contact']
    ordering = ['name']
    date_hierarchy = 'created_at'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'base_salary', 'allowances', 'deductions', 'net_salary']
    list_filter = ['position', 'created_at']
    search_fields = ['name', 'position']
    ordering = ['name']
    readonly_fields = ['net_salary']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position')
        }),
        ('Salary Details', {
            'fields': ('base_salary', 'allowances', 'deductions')
        }),
        ('Calculated', {
            'fields': ('net_salary',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['student', 'amount_paid', 'total_fee', 'balance', 'payment_date']
    list_filter = ['payment_date']
    search_fields = ['student__name']
    ordering = ['-payment_date']
    date_hierarchy = 'payment_date'
    autocomplete_fields = ['student']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'status', 'date']
    list_filter = ['status', 'date']
    search_fields = ['student__name']
    ordering = ['-date']
    date_hierarchy = 'date'
    autocomplete_fields = ['student']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone']
    list_filter = ['role']
    search_fields = ['user__username', 'user__email']


class ReceiptItemInline(admin.TabularInline):
    model = ReceiptItem
    extra = 1


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'student', 'total_amount', 'date', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['receipt_number', 'student__name']
    ordering = ['-date']
    date_hierarchy = 'date'
    autocomplete_fields = ['student']
    inlines = [ReceiptItemInline]
    readonly_fields = ['total_amount']
