from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_wall',
        {
            'title': '鐵窗簾',
            'desc': '放置的牆壁的數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:glass','minecraft:.*_wall']),
    ))
