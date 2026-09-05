from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_rails',
        {
            'title': '鐵路公司',
            'desc': '放置的鐵路數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:.*rail'])
    ))
