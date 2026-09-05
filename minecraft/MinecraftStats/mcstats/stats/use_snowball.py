from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_snowball',
        {
            'title': '雪球大戰!',
            'desc': '丟雪球次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:snowball'])
    ))
