from django.db import models

# Create your models here.

# Common table
# Client details table
class ClientDetails(models.Model):
    name = models.CharField
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    query = models.TextField()

# Employee who visit the site details
class VisitEmployee(models.Model):
    serialNumber = models.IntegerField()
    employeeName = models.CharField()
    employeePhone = models.IntegerField()
    date = models.DateField()

# Quotation Details
class Quotation(models.Model):
    serialNumber: models.IntegerField()
    particular: models.CharField()
    rate = models.FloatField()
    quantity = models.FloatField()
    amount = models.FloatField()
    totalAmount = models.FloatField()

# Expenses table
class Expenses(models.Model):
    serialNumber = models.IntegerField()
    description = models.TextField()
    amount = models.FloatField()

# Invoice status 
class InvoiceStatus(models.Model):
    date: models.DateField()
    amount: models.FloatField()
    status: models.BooleanField()
    remark: models.TextField()

class Approval(models.Model):
    status: models.BooleanField()
    
#  repair and maintainance
# work status

class WorkStatus(models.Model):
    serialNumber: models.IntegerField()
    workCompleted: models.FloatField()
    employeeName: models.CharField()
    employeePhone: models.IntegerField()
    date: models.DateField()
    remark: models.TextField()

# payment status (to be received)
class PaymentRnM(models.Model):
    totalAmountToReceive: models.FloatField()
    receivedAmount: models.FloatField()
    balanceAmount: models.FloatField()

# Disposal table
# collect status
class CollectStatus(models.Model):
    serialNumber: models.IntegerField()
    employeeName: models.CharField()
    employeephone: models.IntegerField()
    date: models.DateField()

# sold or not at the site
class SoldAtSite(models.Model):
    serialNumber: models.IntegerField()
    particular: models.CharField()
    rate = models.FloatField()
    quantity = models.FloatField()
    amount = models.FloatField()
    totalAmountToReceive = models.FloatField()
    totalReceived: models.FloatField()
    balanceAmount: models.FloatField()

class PaymentDisposal(models.Model):
    serialNumber: models.IntegerField()
    date: models.DateField()
    chequeOrDdno: models.CharField()
    totalAmountToPay: models.FloatField()
    paidAmount: models.FloatField()
    balanceAmount: models.FloatField()

