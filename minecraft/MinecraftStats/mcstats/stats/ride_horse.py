from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_horse',
        {
            'title': '騎兵',
            'desc': '騎馬的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:horse_one_cm'])
    ))
