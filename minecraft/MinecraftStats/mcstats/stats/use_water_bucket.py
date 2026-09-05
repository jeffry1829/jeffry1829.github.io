from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_water_bucket',
        {
            'title': '水道',
            'desc': '傾倒水桶次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:water_bucket'])
    ))
