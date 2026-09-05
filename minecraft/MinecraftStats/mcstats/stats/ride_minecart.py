from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_minecart',
        {
            'title': '公共運輸',
            'desc': '搭礦車的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:minecart_one_cm'])
    ))
