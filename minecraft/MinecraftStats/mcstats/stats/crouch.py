from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'crouch',
        {
            'title': '蛇行',
            'desc': '蹲下走過的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:crouch_one_cm'])
    ))
