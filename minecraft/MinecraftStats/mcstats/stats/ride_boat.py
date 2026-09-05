from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_boat',
        {
            'title': '水手',
            'desc': '划船的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:boat_one_cm'])
    ))
