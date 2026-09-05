from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'dive',
        {
            'title': '跳水家',
            'desc': '跳水的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_under_water_one_cm'])
    ))
