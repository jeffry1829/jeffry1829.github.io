from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'climb',
        {
            'title': '爬山專家',
            'desc': '爬過山的總高度',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:climb_one_cm'])
    ))
