from django.db import models
from rooms.models import Room
# Create your models here.
from django.utils import timezone

TEMPERATURE = 1
PRESSURE = 2
NFC = 3
TYPES = [(TEMPERATURE, 'temperature'), (PRESSURE, 'pressure'), (NFC, 'nfc')]

class Node(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    parent_node_id = models.ForeignKey("self", on_delete=models.CASCADE)
    
    type = models.IntegerField(choices=TYPES, default=TEMPERATURE)

    SENSOR = 1
    ACUTATOR = 2
    MASTER = 3
    MODES = [(SENSOR, 'sensor'), (ACUTATOR, 'acutator'), (MASTER, 'master')]
    mode = models.IntegerField(choices=MODES, default=SENSOR)

    created_at = models.DateTimeField('date created', default=timezone.now)

class NodeData(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    node_data = models.BigIntegerField()
    node_type = models.IntegerField(choices=TYPES, default=TEMPERATURE)
    created_at = models.DateTimeField('date created', default=timezone.now)
    timestamp = models.BigIntegerField(null=True)
