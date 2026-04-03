from django import forms
from django.forms import inlineformset_factory
from .models import Student, Employee, Fee, Attendance, Receipt, ReceiptItem


class StudentForm(forms.ModelForm):
    """Form for adding/editing students."""
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'parent_name', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter student full name'
            }),
            'student_class': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Grade 10, Class A'
            }),
            'parent_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter parent name'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter phone number'
            }),
        }


class EmployeeForm(forms.ModelForm):
    """Form for adding/editing employees."""
    class Meta:
        model = Employee
        fields = ['name', 'position', 'base_salary', 'allowances', 'deductions']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter employee name'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Teacher, Administrator'
            }),
            'base_salary': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter base salary',
                'step': '0.01'
            }),
            'allowances': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter allowances',
                'step': '0.01'
            }),
            'deductions': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter deductions',
                'step': '0.01'
            }),
        }


class FeeForm(forms.ModelForm):
    """Form for recording fee payments."""
    class Meta:
        model = Fee
        fields = ['student', 'amount_paid', 'total_fee', 'payment_date']
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select'
            }),
            'amount_paid': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter amount paid',
                'step': '0.01'
            }),
            'total_fee': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter total fee amount',
                'step': '0.01'
            }),
            'payment_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set today's date as initial value
        from datetime import date
        self.fields['payment_date'].initial = date.today()


class AttendanceForm(forms.ModelForm):
    """Form for marking attendance."""
    class Meta:
        model = Attendance
        fields = ['student', 'status', 'date']
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set today's date as initial value
        from datetime import date
        self.fields['date'].initial = date.today()


class ReceiptForm(forms.ModelForm):
    """Form for creating receipts."""
    class Meta:
        model = Receipt
        fields = ['receipt_number', 'student', 'date']
        widgets = {
            'receipt_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter receipt number'
            }),
            'student': forms.Select(attrs={
                'class': 'form-select'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import date
        self.fields['date'].initial = date.today()


class ReceiptItemForm(forms.ModelForm):
    """Form for individual receipt items."""
    class Meta:
        model = ReceiptItem
        fields = ['description', 'amount']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter description'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter amount',
                'step': '0.01'
            }),
        }


# Create formset for receipt items
ReceiptItemFormSet = inlineformset_factory(
    Receipt,
    ReceiptItem,
    form=ReceiptItemForm,
    extra=3,  # Show 3 empty forms by default
    can_delete=True
)
