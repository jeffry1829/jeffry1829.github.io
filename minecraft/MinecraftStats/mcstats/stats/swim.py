from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'swim',
        {
            'title': '游泳健將',
            'desc': '游泳的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:swim_one_cm'])
    ))
