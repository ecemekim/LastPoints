from points.models import NavigationRecord, Vehicle

from django.http import JsonResponse

from datetime import datetime, timedelta


def get_points(request):
    # First, adding some dummy data into postgres db.

    data = [("00 ABC 99", datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S'), 32.32, 32.32),
            ("99 XYZ 000", datetime.strptime("2021-03-17 18:00:00", '%Y-%m-%d %H:%M:%S'), 33.33, 33.33),
            ("11 KLM 57", datetime.strptime("2021-03-17 16:10:06", '%Y-%m-%d %H:%M:%S'), 55.55, 55.55),
            ("57 KLM 57", datetime.strptime("2021-03-17 00:00:00", '%Y-%m-%d %H:%M:%S'), 66.66, 66.66),
            ("57 KLM 57", datetime.strptime("2021-03-15 00:00:00", '%Y-%m-%d %H:%M:%S'), 11.11, 11.11),
            ("00 ABC 99", datetime.strptime("2021-03-15 16:21:20", '%Y-%m-%d %H:%M:%S'), 57.57, 57.57),
            ("11 KLM 57", datetime.strptime("2021-03-17 17:34:55", '%Y-%m-%d %H:%M:%S'), 34.34, 34.34),
            ("99 XYZ 000", datetime.strptime("2021-03-17 17:52:20", '%Y-%m-%d %H:%M:%S'), 22.22, 22.22)]

    unique_vehicles = []
    for row in data:
        unique_vehicles.append(row[0])

    unique_vehicles = list(set(unique_vehicles))

    for v in unique_vehicles:
        if Vehicle.objects.filter(plate=v).exists():
            continue
        else:
            d = Vehicle(plate=v)
            d.save()

    for row in data:
        d = NavigationRecord(
            vehicle_id=Vehicle.objects.filter(plate=row[0])[0].id,
            datetime=row[1],
            latitude=row[2],
            longitude=row[3])
        d.save()

    # Second, getting last 48 hours navigation data for each vehicle.

    points = NavigationRecord.objects.all().select_related('vehicle').filter(
        datetime__gte=datetime.now() - timedelta(hours=48)).values()

    response = JsonResponse({"Last Points": list(points)})

    return response
