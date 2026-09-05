from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_flint',
        {
            'title': '縱火狂',
            'desc': '用打火石點火次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:flint_and_steel'])
    ))
