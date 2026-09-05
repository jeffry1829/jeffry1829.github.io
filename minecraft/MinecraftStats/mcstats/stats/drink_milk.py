from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'drink_milk',
        {
            'title': '奶桶',
            'desc': '喝過的牛奶桶數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:milk_bucket'])
    ))
