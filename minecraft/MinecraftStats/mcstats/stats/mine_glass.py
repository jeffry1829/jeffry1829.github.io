from mcstats import mcstats
mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_glass',
        {
            'title': '玻璃破壞者',
            'desc': '破壞的玻璃的數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],
            ['minecraft:glass','minecraft:.*glass_pane','minecraft:.*stained_glass']),
    ))
