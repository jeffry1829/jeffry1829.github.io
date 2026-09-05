from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_honey_bottle',
        {
            'title': '小熊維尼',
            'desc': '飲用蜂蜜罐次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:honey_bottle']),
        2200 # honey added in 19w34a
    ))
