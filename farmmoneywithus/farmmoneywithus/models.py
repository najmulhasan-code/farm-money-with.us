from django.db import models

class Location(models.Model):
    TERRAIN_CHOICES = [
        ('TU', 'Tundra'),
        ('PL', 'Plains'),
        # ... Add other terrain types as necessary
    ]
    terrain_type = models.CharField(max_length=2, choices=TERRAIN_CHOICES, default='PL')

    def __str__(self):
        return self.get_terrain_type_display()


class Climate(models.Model):
    temperature = models.FloatField()  # Assuming temperature in Celsius
    precipitation = models.FloatField()  # Assuming precipitation in mm

    def __str__(self):
        return f'Temperature: {self.temperature}°C, Precipitation: {self.precipitation}mm'


class MarketCondition(models.Model):
    demand = models.FloatField()  # Assuming a scale of 0 to 100
    supply = models.FloatField()  # Assuming a scale of 0 to 100
    market_price = models.FloatField()  # Assuming price per unit in USD

    def __str__(self):
        return f'Demand: {self.demand}, Supply: {self.supply}, Market Price: ${self.market_price}'


class SoilType(models.Model):
    SOIL_TYPE_CHOICES = [
        ('CL', 'Clay'),
        ('LO', 'Loam'),
        ('SA', 'Sand'),
        # ... Add other soil types as necessary
    ]
    soil_type = models.CharField(max_length=2, choices=SOIL_TYPE_CHOICES, default='LO')

    def __str__(self):
        return self.get_soil_type_display()


class Crop(models.Model):
    name = models.CharField(max_length=100)
    # ... Other relevant fields like expected yield, growth period, etc.

    def __str__(self):
        return self.name


class Farm(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    climate = models.ForeignKey(Climate, on_delete=models.CASCADE)
    market_condition = models.ForeignKey(MarketCondition, on_delete=models.CASCADE)
    soil_type = models.ForeignKey(SoilType, on_delete=models.CASCADE)
    # ... Other relevant fields

    def __str__(self):
        return f'Farm at {self.location}, Soil Type: {self.soil_type}'

