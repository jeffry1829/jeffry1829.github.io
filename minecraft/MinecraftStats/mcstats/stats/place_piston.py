from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_piston',
        {
            'title': '機械動力學',
            'desc': '放置的活塞數量',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.*piston']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.*piston'])),
    ))
