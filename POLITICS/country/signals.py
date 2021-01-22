import datetime


def process_after_pm_insert(sender, instance, **kwargs):
    from .models import PMs, PMsHistory
    current_time = datetime.datetime.now()
    pms_history_obj = PMsHistory()
    pms_history_obj.name = instance.name
    pms_history_obj.pm_id = instance.pm_id
    pms_history_obj.age = instance.age
    pms_history_obj.party = instance.party
    pms_history_obj.country_id = instance.country_id
    pms_history_obj.time_stamp = current_time
    pms_history_obj.status = 'Active'
    pms_history_obj.save()


def process_before_pm_delete(sender, instance, **kwargs):
    from .models import PMs, PMsHistory
    current_time = datetime.datetime.now()
    pms_history_obj = PMsHistory()
    pms_history_obj.name = instance.name
    pms_history_obj.pm_id = instance.pm_id
    pms_history_obj.age = instance.age
    pms_history_obj.party = instance.party
    pms_history_obj.country_id = instance.country_id
    pms_history_obj.time_stamp = current_time
    pms_history_obj.status = 'Deactive'
    pms_history_obj.save()


def process_after_country_insert(sender, instance, **kwargs):
    from .models import CountryHistory
    current_time = datetime.datetime.now()
    country_history_obj = CountryHistory()
    country_history_obj.name = instance.name
    country_history_obj.country_id = instance.country_id
    country_history_obj.country_status = 'Active'
    country_history_obj.time_stamp = current_time
    country_history_obj.save()


def process_after_country_delete(sender, instance, **kwargs):
    from .models import CountryHistory
    current_time = datetime.datetime.now()
    country_history_obj = CountryHistory()
    country_history_obj.name = instance.name
    country_history_obj.country_id = instance.country_id
    country_history_obj.country_status = 'Deactive'
    country_history_obj.time_stamp = current_time
    country_history_obj.save()