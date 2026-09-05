from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_dimensional',
        {
            'title': '火星任務',
            'desc': '挖過的地獄石/終界石的數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:end_stone']),
            mcstats.StatReader(['minecraft:mined','minecraft:netherrack'])
        ])
    ))
