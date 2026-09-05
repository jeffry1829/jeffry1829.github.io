from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_brewing_stand',
        {
            'title': '釀造師',
            'desc': '使用釀造台的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_brewingstand']),
    ))
