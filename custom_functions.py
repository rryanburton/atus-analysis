import re


def data_columns(data, activity):
    return [column for column in data.columns if re.match(activity, column)]


def ave_time(data, activity):
    cols = data_columns(data, activity)
    activity_data = data[cols]
    activity_sum = activity_data.sum(axis=1)
    data = data[['stat_weight']]
    data['minutes'] = activity_sum
    data['weighted_time'] = data.stat_weight * data.minutes
    return data.weighted_time.sum() / data.stat_weight.sum()
