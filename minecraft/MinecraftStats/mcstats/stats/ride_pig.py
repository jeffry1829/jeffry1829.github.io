from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_pig',
        {
            'title': '因為我勇！',
            'desc': '騎豬的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:pig_one_cm'])
    ))
