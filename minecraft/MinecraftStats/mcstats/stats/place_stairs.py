from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_stairs',
        {
            'title': '樓梯工',
            'desc': '建造樓梯的數量',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.+_stairs']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.+_stairs'])),
    ))
