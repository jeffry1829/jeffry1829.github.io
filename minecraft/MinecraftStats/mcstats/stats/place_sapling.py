from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_sapling',
        {
            'title': '植樹家',
            'desc': '種樹的數量',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.+_sapling']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.+_sapling'])),
    ))
