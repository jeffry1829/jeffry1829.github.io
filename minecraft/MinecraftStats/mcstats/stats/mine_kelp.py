from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_kelp',
        {
            'title': '海帶農',
            'desc': '挖過的海帶數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:kelp']),
            mcstats.StatReader(['minecraft:mined','minecraft:kelp_plant']),
        ]),
        1467 # kelp added in 18w07a
    ))
