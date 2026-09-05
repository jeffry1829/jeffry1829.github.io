from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_book',
        {
            'title': '暢銷作家',
            'desc': '寫書數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:writable_book'])
    ))
