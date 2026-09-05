from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_banner',
        {
            'title': '政治宣傳',
            'desc': '放置的旗幟數量',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.*banner']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.*banner'])),
    ))
