""" This is the serializers file, these exist to take data from the database models and convet 
it to JSON, and possibly, if necesarry, perform validations """
from rest_framework import serializers
from heatster.models import (Record, Room, Schedule, Setting, Vacation, Valve,
                             Weekday)


class WeekdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekday
        fields = [
            'id',
            'name'
        ]

        read_only_fields = ['name']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'current_temp',
            'set_temp'
        ]

        read_only_fields = ['room_id']

        
class ValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valve
        fields = [
            'id',
            'room_id',
            'current_temp',
            'set_temp'
        ]


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'room_id',
            'weekday_id',
            'temperature'
        ]

        read_only_fields = ['room_id']


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'id',
            'room_id',
            'temperature',
            'time'
        ]


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = [
            'id',
            'start_date',
            'end_date'
        ]


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = [
            'id',
            'vacation_temp',
            'sleep_temp',
            'sleep_start',
            'sleep_end'
        ]
