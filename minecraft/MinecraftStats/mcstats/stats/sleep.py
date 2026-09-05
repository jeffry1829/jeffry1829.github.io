from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'sleep',
        {
            'title': '睡神',
            'desc': '睡覺時間',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:sleep_in_bed'])
    ))
