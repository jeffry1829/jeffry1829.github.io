from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_nether_wart',
        {
            'title': '地獄農家',
            'desc': '收獲的地獄疙瘩數量',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:picked_up','minecraft:nether_wart']),
            mcstats.StatReader(['minecraft:used','minecraft:nether_wart'])
        )
    ))
