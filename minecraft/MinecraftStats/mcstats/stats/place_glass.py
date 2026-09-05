from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_glass',
        {
            'title': '玻璃工',
            'desc': '放置的玻璃數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:glass','minecraft:.*glass_pane','minecraft:.*stained_glass']),
    ))
