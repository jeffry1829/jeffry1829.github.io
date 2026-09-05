from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_crossbow',
        {
            'title': '神槍手',
            'desc': '努箭射擊次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:crossbow']),
        1901 # crossbows added in 18w43a
    ))
