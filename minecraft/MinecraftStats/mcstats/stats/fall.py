from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'fall',
        {
            'title': '高空彈跳',
            'desc': '落下的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:fall_one_cm'])
    ))
