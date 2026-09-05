from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_turtle_helmet',
        {
            'title': '烏龜頭',
            'desc': '製造的烏龜頭盔數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:turtle_helmet']),
        ]),
        1467 # turtle helmets introduced in 18w07a
    ))
