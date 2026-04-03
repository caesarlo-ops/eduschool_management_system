from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('attendance/', views.attendance, name='attendance'),
    path('fees/', views.fees, name='fees'),
    path('payroll/', views.payroll, name='payroll'),
    path('payslip/', views.generate_payslip, name='payslip'),
    # Receipt URLs
    path('receipts/', views.receipts, name='receipts'),
    path('receipts/create/', views.create_receipt, name='create_receipt'),
    path('receipts/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    # Export URL
    path('fees/export-debtors/', views.export_debtors, name='export_debtors'),
]
