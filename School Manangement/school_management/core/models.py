from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """Student model for storing student information."""
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50, blank=True, null=True)
    parent_name = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Employee model for storing staff information."""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.name} - {self.position}"

    @property
    def net_salary(self):
        """Calculate net salary."""
        return self.base_salary + self.allowances - self.deductions


class Fee(models.Model):
    """Fee model for storing fee payment records."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-payment_date']
        verbose_name = 'Fee Payment'
        verbose_name_plural = 'Fee Payments'

    def __str__(self):
        return f"{self.student.name} - ${self.amount_paid}"

    def save(self, *args, **kwargs):
        """Auto-calculate balance before saving."""
        self.balance = self.total_fee - self.amount_paid
        super().save(*args, **kwargs)


class Attendance(models.Model):
    """Attendance model for storing attendance records."""
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Excused', 'Excused'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Present')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'student__name']
        verbose_name = 'Attendance Record'
        verbose_name_plural = 'Attendance Records'
        unique_together = ['student', 'date']

    def __str__(self):
        return f"{self.student.name} - {self.status} on {self.date}"


class UserProfile(models.Model):
    """Extended user profile for role management."""
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='teacher')
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_teacher(self):
        return self.role == 'teacher'


class Receipt(models.Model):
    """Receipt model for storing payment receipts."""
    receipt_number = models.CharField(max_length=50, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='receipts')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'receipt_number']
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'

    def __str__(self):
        return f"Receipt #{self.receipt_number} - {self.student.name}"

    def calculate_total(self):
        """Calculate total from all receipt items."""
        total = sum(item.amount for item in self.items.all())
        self.total_amount = total
        return total


class ReceiptItem(models.Model):
    """Receipt item model for individual line items on a receipt."""
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Receipt Item'
        verbose_name_plural = 'Receipt Items'

    def __str__(self):
        return f"{self.description} - ${self.amount}"
