from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_ender_eye',
        {
            'title': '千里眼',
            'desc': '終界之眼使用次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:ender_eye'])
    ))
