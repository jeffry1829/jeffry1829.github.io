from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_fireworks',
        {
            'title': '新年快樂!',
            'desc': '發射煙火數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:firework_rocket'])
    ))
