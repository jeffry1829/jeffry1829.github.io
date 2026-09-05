from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'walk_on_water',
        {
            'title': '耶穌',
            'desc': '在水上行走距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_on_water_one_cm'])
    ))
