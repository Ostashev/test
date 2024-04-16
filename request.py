from datetime import datetime, timedelta
from typing import Dict, List

from database import connect_to_mongo


async def aggregate_data(dt_from: datetime, dt_upto: datetime, group_type: str) -> Dict[str, List[int]]:

    collection = await connect_to_mongo()
    
    format_string = ""
    if group_type == "day":
        format_string = "%Y-%m-%d"
    elif group_type == "month":
        format_string = "%Y-%m-01"
    elif group_type == "hour":
        format_string = "%Y-%m-%dT%H:00:00"

    pipeline = [
        {
            "$match": {
                "dt": {"$gte": dt_from, "$lte": dt_upto}
            }
        },
        {
            "$group": {
                "_id": {"$dateToString": {"format": format_string, "date": "$dt"}},
                "total": {"$sum": "$value"}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    cursor = collection.aggregate(pipeline)

    dataset = []
    labels = []

    current_date = dt_from
    while current_date <= dt_upto:
        labels.append(current_date.strftime(format_string))
        dataset.append(0)
        if group_type == "hour":
            current_date += timedelta(hours=1)
        elif group_type == "day":
            current_date += timedelta(days=1)
        elif group_type == "month":
            current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)

    async for document in cursor:
        total_value = document["total"]
        total_date = document["_id"]
        index = labels.index(total_date)
        dataset[index] = total_value

    if group_type == 'day' or group_type == 'month':
        return {"dataset": [dataset], "labels": [[label+'T00:00:00' for label in labels]]}

    return {"dataset": [dataset], "labels": [labels]}
