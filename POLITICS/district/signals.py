def signal_after_adding_district(sender, instance, **kwargs):
    print("signal after adding district is calling")


def signal_before_adding_district(sender, instance, **kwargs):
    print("signal before adding district is calling")