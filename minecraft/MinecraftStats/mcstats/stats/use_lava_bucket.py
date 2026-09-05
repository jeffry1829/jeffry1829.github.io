from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_lava_bucket',
        {
            'title': '汽油彈',
            'desc': '傾倒岩漿次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:lava_bucket'])
    ))
