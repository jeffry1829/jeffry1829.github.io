from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'trade',
        {
            'title': '商人',
            'desc': '和NPC交易的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:traded_with_villager'])
    ))
