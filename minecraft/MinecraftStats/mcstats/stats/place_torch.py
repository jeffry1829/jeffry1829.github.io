from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_torch',
        {
            'title': '燃燒自己，照亮他人',
            'desc': '放置的火把數量',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:used','minecraft:torch']),
            mcstats.StatReader(['minecraft:mined','minecraft:torch']))
    ))
