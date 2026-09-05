from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_clock',
        {
            'title': '鐘錶師',
            'desc': '製造的時鐘數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:clock']),
    ))
