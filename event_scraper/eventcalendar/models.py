from django.db import models

class Address(models.Model):
    """
    Represents the address of a given venue.
    """
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

class Venue(models.Model):
    """
    Represents a venue where events may take place
    """
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True, default='')

    # TODO: add the following
    # operating_hours - should display unique hours of
        # operation for each day of the week

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    date_removed = models.DateTimeField(blank=True, null=True)

class Event(models.Model):
    """docstring for Event"""
    def __str__(self):
        return self.name
    name = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(blank=True, null=True, default='')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey(Venue, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    date_removed = models.DateTimeField(blank=True, null=True)

    def duration(self):
        return self.end_date - self.start_date