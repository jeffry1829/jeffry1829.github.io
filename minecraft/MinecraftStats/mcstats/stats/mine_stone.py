from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_stone',
        {
            'title': '地底之王',
            'desc': '挖過的各種石頭',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:stone']),
            mcstats.StatReader(['minecraft:mined','minecraft:diorite']),
            mcstats.StatReader(['minecraft:mined','minecraft:andesite']),
            mcstats.StatReader(['minecraft:mined','minecraft:granite']),
        ])
    ))
