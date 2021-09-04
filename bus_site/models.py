from django.db import models

# Create your models here.

class Bus(models.Model):
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return '%s From %s To %s' %(self.id,self.source,self.dest)


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=12, help_text='Maximum 12 characters')

    def __str__(self):
        return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    
    userid =models.ForeignKey(User, on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus, on_delete=models.CASCADE)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return 'User number %s %s Bus number %s' %(self.userid,self.TICKET_STATUSES[self.status],self.busid)
