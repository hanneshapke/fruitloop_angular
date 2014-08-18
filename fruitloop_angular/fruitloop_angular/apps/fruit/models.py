import sys

from django.db import models
from django_extensions.db.models import TimeStampedModel

from pygeocoder import Geocoder


class FruitType(TimeStampedModel):

    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Fruit Types"

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)


class FruitLocation(TimeStampedModel):

    address = models.CharField(
        max_length=50)
    comment = models.TextField(
        blank=True, null=True)
    fruit_type = models.ForeignKey(FruitType)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=7,
        blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7,
        blank=True, null=True)

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Fruit Locations"

    def save(self, *args, **kwargs):
        try:
            # get the geocoding results
            results = Geocoder.geocode(self.address)
            # correct the address spelling
            self.address = results[0].formatted_address.encode('utf-8')
            self.latitude = results[0].coordinates[0]
            self.longitude = results[0].coordinates[1]
        except Exception:
            print "Oops!  Couldn't geocode address because of %s" \
                % sys.exc_info()[0]

        super(FruitLocation, self).save(*args, **kwargs)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s tree at %s' % (self.fruit_type, self.address)
