from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_cactus',
        {
            'title': '仙人掌農',
            'desc': '種過的仙人掌數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:cactus'])
    ))
