from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_cookie',
        {
            'title': '餅乾怪獸',
            'desc': '吃過的餅乾數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:cookie'])
    ))
