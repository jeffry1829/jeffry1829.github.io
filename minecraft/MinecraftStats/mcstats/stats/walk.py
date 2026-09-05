from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'walk',
        {
            'title': '旅行者',
            'desc': '行走距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_one_cm'])
    ))
