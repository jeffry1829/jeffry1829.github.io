from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_smoker',
        {
            'title': '主廚',
            'desc': '使用煙燻爐的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_smoker']),
        1919 # smokers usable since 18w50a
    ))
