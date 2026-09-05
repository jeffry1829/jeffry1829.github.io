from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bread',
        {
            'title': '烘培師',
            'desc': '製造的麵包、蛋糕、餅乾數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:bread']),
            mcstats.StatReader(['minecraft:crafted','minecraft:cake']),
            mcstats.StatReader(['minecraft:crafted','minecraft:cookie']),
        ])
    ))
