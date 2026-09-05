from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_ender_pearl',
        {
            'title': '轉位者',
            'desc': '終界珍珠使用次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:ender_pearl'])
    ))
