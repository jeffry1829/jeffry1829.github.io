from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_dirt',
        {
            'title': '土包子',
            'desc': '放置泥土方塊數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:dirt'])
    ))
