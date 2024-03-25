def format_duration(seconds):
    if seconds == 0:
        return "now"

    conversions = [
        ('year', 365 * 24 * 60 * 60),
        ('day', 24 * 60 * 60),
        ('hour', 60 * 60),
        ('minute', 60),
        ('second', 1)
    ]

    formatted_components = []

    for unit, conversion in conversions:
        value = seconds // conversion
        if value > 0:
            formatted_components.append('{} {}'.format(value, unit if value == 1 else unit + 's'))
        seconds %= conversion

    if len(formatted_components) > 1:
        return ', '.join(formatted_components[:-1]) + ' and ' + formatted_components[-1]
    else:
        return formatted_components[0]
